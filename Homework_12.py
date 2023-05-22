import json


class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}

    def load_data(self):
        try:
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f)

    @staticmethod
    def make_file_storage(file_path):
        storage = FileStorage(file_path)
        storage.load_data()
        return storage

    def __enter__(self):
        self.load_data()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save_data()


class Pagination:
    def __init__(self, iterable, page_size=3):
        self.iterable = iterable
        self.page_size = page_size
        self.current_page = 0

    def __iter__(self):
        return self

    def __next__(self):
        start = self.current_page * self.page_size
        end = start + self.page_size
        items = self.iterable[start:end]

        if not items:
            raise StopIteration

        self.current_page += 1
        return items

    def go_to_page(self, page):
        self.current_page = page

    def go_to_next_page(self):
        self.current_page += 1

    def go_to_previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1


class App:
    def __init__(self, storage):
        self.storage = storage

    def add_course(self):
        course_name = input("Enter course name: ")
        self.storage.data[course_name] = []
        print(f"Course '{course_name}' added successfully.")

    def add_student(self):
        course_name = input("Enter course name: ")
        student_name = input("Enter student name: ")
        if course_name in self.storage.data:
            self.storage.data[course_name].append(student_name)
            print(f"Student '{student_name}' added to course '{course_name}' successfully.")
        else:
            print(f"Course '{course_name}' does not exist.")

    def remove_course(self):
        course_name = input("Enter course name: ")
        if course_name in self.storage.data:
            del self.storage.data[course_name]
            print(f"Course '{course_name}' removed successfully.")
        else:
            print(f"Course '{course_name}' does not exist.")

    def remove_student(self):
        course_name = input("Enter course name: ")
        student_name = input("Enter student name: ")
        if course_name in self.storage.data:
            if student_name in self.storage.data[course_name]:
                self.storage.data[course_name].remove(student_name)
                print(f"Student '{student_name}' removed from course '{course_name}' successfully.")
            else:
                print(f"Student '{student_name}' is not enrolled in course '{course_name}'.")
        else:
            print(f"Course '{course_name}' does not exist.")

    def show_courses(self):
        if not self.storage.data:
            print("No courses found.")
        else:
            print("List of courses:")
            courses = list(self.storage.data.keys())
            paginated_courses = Pagination(courses)

            for page in paginated_courses:
                for course_name in page:
                    print(course_name)

    def run(self):
        while True:
            print("Menu:")
            print("1. Add course")
            print("2. Add student to course")
            print("3. Delete course")
            print("4. Delete student from course")
            print("5. Show all courses")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                self.add_course()
            elif choice == "2":
                self.add_student()
            elif choice == "3":
                self.delete_course()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                self.show_courses()
            elif choice == "6":
                print("Saving changes and exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

        if __name__ == '__main__':
            file_path = input("Enter file path: ")
            storage = FileStorage.make_file_storage(file_path)
            app = App(storage)
            app.run()
