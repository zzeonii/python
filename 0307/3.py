>>> class Student:
    def __init__(inst,name,age):
        inst.name=name
        inst.age=age
    def getName(inst):
        return inst.name
    
>>> s4=Student('Tom',19)
>>> s4.name
'Tom'
>>> s4.age
19
>>> s4
<__main__.Student object at 0x000001B7C2C961A0>
>>> s4.getName()
'Tom'
>>> class Student:
    def __init__(inst,name,age):
        inst.name=name
        inst.age=age
    def getName(inst):
        return inst.name
    def getAge(inst):
        return inst.age
    def setAge(inst,newAge):
        inst.age=newAge
        
>>> s1=Student('Jane',19)
>>> s1.age
19
>>> s1.getAge()
19
>>> s1.setAge(s1.getAge()+1)
>>> s1.getAge()
20
>>> s1
<__main__.Student object at 0x000001B7C2CDB910>
>>> *s1,
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Value after * must be an iterable, not Student
>>> 
