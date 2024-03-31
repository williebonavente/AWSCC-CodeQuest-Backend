class Student:
    def __init__(self, name, age,
                 is_enrolled, classes, offenses):
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses

    def __str__(self) -> str:
        return f'Student Name: {self.name}\nAge: {self.age}\nStatus: {"Enrolled" if self.is_enrolled is True else "Shiftie"}\nClasses: {self.classes}\nOffenses: {self.offenses}\n'
    


student1 = Student("Juan Dela Cruz", 19, True, [], [])
student2 = Student("Willie M. Bonavente", 19, False, ['Attributes'], ['Offended'])
print(student1.__str__())
print(student2.__str__())
