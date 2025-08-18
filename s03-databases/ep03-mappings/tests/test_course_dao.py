import pytest

from src.domain.dao.course_dao import CourseDao
from src.domain.db import Base, engine

from src.domain.model.courses import Course

COURSE_DATA = [
    {"name": "Course 1", "description": "Description 1", "hours": 10, "id" : 1},
    {"name": "Course 2", "description": "Description 2", "hours": 20, "id" : 2},
]

@pytest.fixture(scope="function", autouse=True)
def course_dao():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    dao = CourseDao()
    with dao.session:
        yield dao

    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def prepare_courses(course_dao):
    for data in COURSE_DATA:
        course_dao.create(
            Course(
                name=data['name'], 
                description=data['description'], 
                hours=data['hours']
            )
        )

@pytest.mark.parametrize("course_data", COURSE_DATA)
def test_create_course(course_dao, course_data):
    course = course_dao.create(Course(name=course_data["name"], description=course_data["description"], hours=course_data["hours"]))
    assert course.id is not None
    assert course.name == course_data["name"]
    assert course.description == course_data["description"]
    assert course.hours == course_data["hours"]

@pytest.mark.usefixtures("prepare_courses")
@pytest.mark.parametrize("course_data", COURSE_DATA)
def test_find_one(course_dao, course_data):
    course = course_dao.find_one(course_data['id'])
    assert course.id == course_data["id"]
    assert course.name == course_data["name"]
    assert course.description == course_data["description"]
    assert course.hours == course_data["hours"]

@pytest.mark.usefixtures("prepare_courses")
@pytest.mark.parametrize("update_data", [
    (1, "Update Name 1", "Update Description 1", 25),
    (2, "Update Name 2", "Update Description 2", 35),
])
def test_update(course_dao, update_data):
    course = Course(id=update_data[0], name=update_data[1], description=update_data[2], hours=update_data[3])
    updated_course = course_dao.update(course)
    assert updated_course.id == update_data[0]
    assert updated_course.name == update_data[1]
    assert updated_course.description == update_data[2]
    assert updated_course.hours == update_data[3]

@pytest.mark.usefixtures("prepare_courses")
@pytest.mark.parametrize("course_data", COURSE_DATA)
def test_search(course_dao, course_data):
    list = course_dao.search({"name" : course_data["name"]})
    assert len(list) == 1

@pytest.mark.usefixtures("prepare_courses")
@pytest.mark.parametrize("id", [1, 2])
def test_delete(course_dao, id:int):
    assert course_dao.delete(id)

@pytest.mark.parametrize("id", [1, 2])
def test_delete_not_found(course_dao, id:int):
    assert not course_dao.delete(id)
