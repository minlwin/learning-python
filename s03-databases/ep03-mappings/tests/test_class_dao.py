from datetime import date
import pytest

from src.domain.dao.class_dao import ClassDao
from src.domain.dao.course_dao import CourseDao
from src.domain.db import Base, engine
from src.domain.model.classes import Class
from src.domain.model.courses import Course

TEST_DATA = [
    {"course_id" : 1, "start_at" : date.today(), "months" : 3, 'id': 1},
    {"course_id" : 2, "start_at" : date.today(), "months" : 4, 'id': 2},
    {"course_id" : 3, "start_at" : date.today(), "months" : 5, 'id': 3},
]

@pytest.fixture(scope="function", autouse=True)
def class_dao():
    # Drop and Create All Tables
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    # Prepare Course
    course_dao = CourseDao()
    with course_dao.session:
        course_dao.create(Course(name="Java Basic", description="Foundation of Java", hours=90))
        course_dao.create(Course(name="Spring Framework", description="Advance course of Java", hours=180))
        course_dao.create(Course(name="React", description="Modern Front End Technology", hours=90))

    # Create ClassDao and Yield it
    dao = ClassDao()
    with dao.session:
        yield dao

    # Clean Up Tables
    Base.metadata.drop_all(engine)

@pytest.fixture
def prepare_classes(class_dao):
    for data in TEST_DATA:
        class_dao.create(Class(
            course_id=data["course_id"],
            start_at=data["start_at"],
            months=data["months"]
        ))        

@pytest.mark.parametrize("data", TEST_DATA)
def test_create(class_dao, data):
    result = class_dao.create(Class(
        course_id=data["course_id"],
        start_at=data["start_at"],
        months=data["months"]
    ))
    assert result.id is not None
    assert result.course.id == data['course_id']
    assert result.start_at == data['start_at']
    assert result.months == data['months']

@pytest.mark.usefixtures("prepare_classes")
@pytest.mark.parametrize("data", TEST_DATA)
def test_find_one(class_dao, data):
    result = class_dao.find_one(data['id'])
    assert result.id == data['id']
    assert result.course.id == data['course_id']
    assert result.start_at == data['start_at']
    assert result.months == data['months']

@pytest.mark.usefixtures("prepare_classes")
@pytest.mark.parametrize("for_update", [
    {"months" : 5, 'id': 1},
    {"months" : 6, 'id': 2},
    {"months" : 4, 'id': 3},
])
def test_update(class_dao, for_update):
    to_update = class_dao.find_one(for_update['id'])
    to_update.months = for_update['months']
    result = class_dao.update(to_update)
    assert result.months == for_update['months']

@pytest.mark.usefixtures("prepare_classes")
@pytest.mark.parametrize("id", [1, 2, 3])
def test_delete(class_dao, id:int):
    assert class_dao.delete(id)