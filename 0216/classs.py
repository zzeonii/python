class Student:
    def __init__(instance, name, age):
        instance.name=name
        instance.age=age
    def get_name(instance):
        return instance.name
    def get_age(instance):
        return instance.age
    def set_age(instance, age):
        instance.age=age
        
student_1=Student('Brad', 21)
student_2=Student('Jane', 25)
student_1.name