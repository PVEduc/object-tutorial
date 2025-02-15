class Student:
    def __init__(self, name: str, major: str, student_id: str):
        self.name = name
        self.major = major
        self.student_id = student_id

class FullTimeStudent(Student):
    def __init__(self, name: str, major: str, student_id: str, credit_hours: int):
        super().__init__(name, major, student_id)
        self.credit_hours = credit_hours

class PartTimeStudent(Student):
    def __init__(self, name: str, major: str, student_id: str, min_hour: int, max_hour: int):
        super().__init__(name, major, student_id)
        self.min_hour = min_hour
        self.max_hour = max_hour

class Lecturer:
    def __init__(self, name: str, lecturer_id: str, department: str):
        self.name = name
        self.lecturer_id = lecturer_id
        self.department = department

class Project:
    def __init__(self, project_name: str, student: Student, supervisor: Lecturer):
        self.project_name = project_name
        self.student = student
        self.supervisor = supervisor
