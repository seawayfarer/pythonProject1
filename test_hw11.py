import unittest
from app import FileStorage, Pagination, Course


class FileStorageTestCase(unittest.TestCase):
    def test_data_structure(self):
        storage = FileStorage('test_data.json')
        storage.data = {'courses': ['Python', 'Java', 'C++']}

        storage.save_data()

        with open('test_data.json', 'r') as f:
            data = f.read()
            self.assertEqual(data, '{"courses": ["Python", "Java", "C++"]}')

    def test_load_courses(self):
        storage = FileStorage('test_data.json')

        storage.load_data()

        self.assertEqual(storage.data, {'courses': ['Python', 'Java', 'C++']})

    def tearDown(self):
        # Clean up the test data file
        with open('test_data.json', 'w') as f:
            f.write('')


class PaginationTestCase(unittest.TestCase):
    def test_pagination(self):
        data = [1, 2, 3, 4]

        pagination = Pagination(data, page_size=3)

        self.assertEqual(next(pagination), [1, 2, 3])
        self.assertEqual(next(pagination), [4])

        with self.assertRaises(StopIteration):
            next(pagination)

        pagination.previous()
        self.assertEqual(next(pagination), [1, 2, 3])

        pagination.previous()
        self.assertEqual(next(pagination), [1, 2, 3])

    def test_empty_pagination(self):
        data = []

        pagination = Pagination(data, page_size=3)

        with self.assertRaises(StopIteration):
            next(pagination)

    def test_pagination_with_multiple_of_three(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        pagination = Pagination(data, page_size=3)

        self.assertEqual(next(pagination), [1, 2, 3])
        self.assertEqual(next(pagination), [4, 5, 6])
        self.assertEqual(next(pagination), [7, 8, 9])

    def tearDown(self):
        with open('test_data.json', 'w') as f:
            f.write('')


class CourseTestCase(unittest.TestCase):
    def test_add_student(self):
        course = Course('Python')
        course.add_student('John Doe')

        self.assertEqual(course.get_students(), ['John Doe'])

    def test_get_students(self):
        course = Course('Python')
        course.add_student('John Doe')
        course.add_student('Jane Smith')

        self.assertEqual(course.get_students(), ['John Doe', 'Jane Smith'])

    def tearDown(self):
        # Clean up the test data file
        with open('test_data.json', 'w') as f:
            f.write('')


if __name__ == '__main__':
    unittest.main()
