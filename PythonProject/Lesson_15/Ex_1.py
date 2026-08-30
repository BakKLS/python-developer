"""Задание 1
Разработайте класс Student, который хранит информацию о
студенте: имя, список курсов и оценки. Реализуйте методы для расчета среднего балла и добавления новых курсов.
Создайте группу студентов и найдите студента с лучшей успеваемостью
Добавьте метод для вывода информации о незавершенных курсах
Реализуйте функцию, которая формирует список отличников"""


class Student:
    def __init__(self, name: str):
        self.name = name
        self.courses = []
        self.grades = {}


    def add_course(self, course_name: str, grade: int = None):
        if course_name not in self.courses:
            self.courses.append(course_name)
        if grade is not None:
            self.grades[course_name] = grade


    def get_average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def get_incomplete_courses(self) -> list:
        incomplete = []
        for course in self.courses:
            if course not in self.grades:
                incomplete.append(course)
        return incomplete


def get_top_students(student_group: list) -> list:
    top_students = []
    for student in student_group:
        if student.get_average_grade() >= 4.5:
            top_students.append(student.name)
    return top_students



st1 = Student("Алексей")
st1.add_course("Python", 5)
st1.add_course("Git", 5)
st1.add_course("Базы данных")

st2 = Student("Мария")
st2.add_course("Python", 4)
st2.add_course("Git", 5)

st3 = Student("Иван")
st3.add_course("Python", 3)
st3.add_course("Git", 4)

group = [st1, st2, st3]

best_student = group[0]
for student in group:
    if student.get_average_grade() > best_student.get_average_grade():
        best_student = student

print(f"Студент с лучшей успеваемостью: {best_student.name} (Средний балл: {best_student.get_average_grade():.2f})")
print(f"Незавершенные курсы у {st1.name}: {st1.get_incomplete_courses()}")
print(f"Список отличников группы: {get_top_students(group)}")