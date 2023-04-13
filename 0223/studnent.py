>>> class Student:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
        
>>> class Student:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def Print(self):
        print(self.name, self.age, self.gender)
        
>>> student_1=Student("홍길동",23,"남자")
>>> student_1.print()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'print'
>>> student_1.Print()
홍길동 23 남자
>>> 
