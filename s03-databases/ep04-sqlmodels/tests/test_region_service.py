import pytest
from sqlmodel import SQLModel
from src.model.database import engine
from src.model.entity.region import Region
from src.model.services.region_service import RegionService

TEST_DATA = [
    {"name" : "Yangon", "region" : "South", 'id': 1},
    {"name" : "Mandalay", "region" : "Center", 'id': 2},
    {"name" : "Rakhine", "region" : "West", 'id': 3},
]

@pytest.fixture(scope='function', autouse=True)
def region_service():
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)
    return RegionService(engine=engine)

@pytest.fixture
def prepare_data(region_service):
    for data in TEST_DATA:
        entity = Region(name=data['name'], region=data['region'])
        region_service.create(entity)

@pytest.mark.parametrize("test_data", TEST_DATA)
def test_create(region_service, test_data):
    to_create = Region(name=test_data['name'], region=test_data['region'])
    result = region_service.create(to_create)
    assert result.id is not None
    assert result.name == test_data['name']
    assert result.region == test_data['region']

@pytest.mark.usefixtures('prepare_data')
@pytest.mark.parametrize("test_data", TEST_DATA)
def test_find_one(region_service, test_data):
    result = region_service.find_one(test_data['id'])
    assert result is not None
    assert result.id == test_data['id']
    assert result.name == test_data['name']
    assert result.region == test_data['region']

@pytest.mark.usefixtures('prepare_data')
def test_find_all(region_service):
    result = region_service.find_all()
    assert len(result) == 3

@pytest.mark.usefixtures('prepare_data')
@pytest.mark.parametrize("id", [1, 2, 3])
def test_delete(region_service, id:int):
    assert region_service.delete(id)

@pytest.mark.usefixtures('prepare_data')
@pytest.mark.parametrize("id", [4, 5, 6])
def test_delete_not_found(region_service, id:int):
    assert not region_service.delete(id)
