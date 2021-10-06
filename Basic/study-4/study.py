# -*- coding: utf8 -*-
def create(name,age,collage=None) :
    class Person :
        def __init__(self,name,age) :
            self.name = name
            self.age = age
        
    class Student(Person) :
        def __init__(self,name,age,collage) :
            super().__init__(name,age)
            self.collage = collage

    if collage == None :
        result = Person(name,age)
    else :
        result = Student(name,age,collage)
    return result

go = create("고블럭", 25)
print(go.__dict__, type(go))

stu = create("오준석", 25, "학교")
print(stu.__dict__, type(stu))
