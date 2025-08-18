import pytest

from sqlmodel import SQLModel
from src.model.database import engine
from src.model.entity.region import Region
from src.model.entity.township import Township
from src.model.services.region_service import RegionService
from src.model.services.township_service import TownshipService
from tests.test_region_service import TEST_DATA

REGIONS = [
    {"name" : "Yangon", "region" : "South", 'id': 1},
    {"name" : "Mandalay", "region" : "Center", 'id': 2},
    {"name" : "Rakhine", "region" : "West", 'id': 3},
]

TEST_DATA = [
    {"name": "North Okkalapa", "region_id": 1, 'id': 1},
    {"name": "South Okkalapa", "region_id": 1, 'id': 2},
    {"name": "Hlaing Tharyar", "region_id": 1, 'id': 3},
]

@pytest.fixture(scope='function', autouse=True)
def township_service():
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)

    for region in REGIONS:
        service = RegionService(engine=engine)
        service.create(Region(**region))

    return TownshipService(engine=engine)

@pytest.fixture
def prepare_data(township_service):
    for township in TEST_DATA:
        township_service.create(Township(**township))

@pytest.mark.parametrize("test_data", TEST_DATA)
def test_create(township_service, test_data):
    to_create = Township(name=test_data['name'], region_id=test_data['region_id'])
    result = township_service.create(to_create)
    assert result.id is not None
    assert result.name == test_data['name']
    assert result.region_id == test_data['region_id']

@pytest.mark.usefixtures('prepare_data')
@pytest.mark.parametrize("test_data", TEST_DATA)
def test_find_one(township_service, test_data):
    result = township_service.find_one(test_data['id'])
    assert result is not None
    assert result.id == test_data['id']
    assert result.name == test_data['name']
    assert result.region_id == test_data['region_id']
    assert result.region is not None
    assert result.region.id == test_data['region_id']
    assert result.region.name == REGIONS[test_data['region_id'] - 1]['name']
    assert result.region.region == REGIONS[test_data['region_id'] - 1]['region']

@pytest.mark.usefixtures('prepare_data')
def test_find_by_region(township_service):
    result = township_service.find_by_region(1)
    assert result is not None
    assert len(result) == 3
    assert all(township.region_id == 1 for township in result)

@pytest.mark.usefixtures('prepare_data')
def test_update(township_service):
    to_update = Township(id=1, name="Updated Township", region_id=1)
    result = township_service.update(to_update)
    assert result.id == 1
    assert result.name == "Updated Township"
    assert result.region_id == 1

def test_find_one_not_found(township_service):
    result = township_service.find_one(999)
    assert result is None

@pytest.mark.usefixtures('prepare_data')
def test_delete(township_service):
    result = township_service.delete(1)
    assert result is True
    assert township_service.find_one(1) is None