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


class App:
    def __init__(self, storage):
        self.storage = storage

    def add_course(self):
        course_name = input("Enter course name: ")
        self.storage.data[course_name] = []
        print(f"Course '{course_name}' added successfully.")

    def show_courses(self):
        if not self.storage.data:
            print("No courses found.")
        else:
            print("List of courses:")
            for course_name in self.storage.data:
                print(course_name)

    def run(self):
        while True:
            print("Menu:")
            print("1. Add course")
            print("2. Show all courses")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")
            if choice == "1":
                self.add_course()
            elif choice == "2":
                self.show_courses()
            elif choice == "3":
                print("Saving changes and exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    storage = FileStorage.make_file_storage('path/to/file.json')
    app = App(storage)
    app.run()
