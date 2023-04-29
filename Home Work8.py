class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        return {'first_name': self.first_name, 'last_name': self.last_name}


s = Student('Jhonny', 'Depp')
print(s.info())


class Storage:
    def __init__(self):
        self.words = []

    def add(self, word):
        self.words.append(word)

    def get(self, start):
        filtered_words = [w for w in self.words if w.startswith(start)]
        sorted_words = sorted(filtered_words)
        return sorted_words[:5]


storage = Storage()
storage.add("apple")
storage.add("banana")
storage.add("pear")
storage.add("peach")
storage.add("apricot")
print(storage.get("a"))
print(storage.get("b"))
print(storage.get("p"))


import json


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        return {'first_name': self.first_name, 'last_name': self.last_name}


class Course:
    def __init__(self, Course):
        self.name = Course
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def to_json(self):
        data = {'Course': self.name, 'students': [student.info() for student in self.students]}
        return json.dumps(data)


course = Course('Python Basic')


student1 = Student('Jhonny', 'Depp')
student2 = Student('Vasia', 'Vasilenko')
student3 = Student('Grisha', 'Petrov')
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

json_data = course.to_json()
print(json_data)
