import json
from your_module import FileStorage


def test_save_data(tmp_path):
    # create a temporary file for testing
    file_path = tmp_path / "test_file.json"

    # create an instance of FileStorage and save the data
    storage = FileStorage(file_path)
    storage.data = {"key": "value"}
    storage.save_data()

    # verify that the data has been saved in the file
    with open(file_path, 'r') as f:
        data = json.load(f)
    assert data == {"key": "value"}


from your_module import Pagination


def test_pagination():
    iterable = [1, 2, 3, 4, 5, 6]

    # create an instance of Pagination with a page size of 3
    pager = Pagination(iterable, page_size=3)

    # verify that the first call returns the first page [1, 2, 3]
    assert list(next(pager)) == [1, 2, 3]

    # verify that the second call returns the second page [4, 5, 6]
    assert list(next(pager)) == [4, 5, 6]

    # verify that the third call returns an empty list
    assert list(next(pager)) == []

    # navigate to the previous page
    pager.previous_page()

    # verify that we again receive the first page [1, 2, 3]
    assert list(next(pager)) == [1, 2, 3]


from your_module import Course


def test_add_student():
    course = Course("Math")

    # add a student
    course.add_student("John Doe")

    # verify that the student has been added
    assert "John Doe" in course.students

    # add another student
    course.add_student("Jane Smith")

    # verify that the second student has been added
    assert "Jane Smith" in course.students


def test_remove_student():
    course = Course("Math")

    # add a student
    course.add_student("John Doe")

    # removed student
    course.remove_student("John Doe")

    # verify that the student has been removed
    assert "John Doe" not in course.students
