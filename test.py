# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# user1 = Person(name='Albert', age=12)
# print(user1.name, user1.age)
# user2 = Person(name='Pasha', age=22)
# print(user2.name, user2.age)
# user3 = Person(name='Artem', age=37)
# print(user3.name, user3.age)
#
#


class Animal:
    def __init__(self, anim, sound):
        self.anim = anim
        self.sound = sound

    def make_sound(self):
        return f"{self.anim} издала звук - {self.sound}"


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Cow(Animal):
    pass
qweqwe

