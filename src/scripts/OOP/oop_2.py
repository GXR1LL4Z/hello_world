class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def srednia_ocen(self):
        value = 0
        for student in self.students:
            value = value + student.get_grade()
        return value/len(self.students)

s1 = Student("Tim", 19, 5)
s2 = Student("Greg", 20, 4.5)
course = Course("Math", 20)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.students[1].name)
print(course.srednia_ocen())

