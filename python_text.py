# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # def sinc(x):
# #     return np.where(x == 0, 1.0, np.sin(x)/x)
# #
# # x = np.linspace(-10*np.pi, 10*np.pi, 1000)
# # y = sinc(x)
# #
# # plt.plot(x, y)
# # plt.title(r'$\frac{\sin(x)}{x}$')
# # plt.grid(True)
# # plt.show()
# # class Car():
# #     def colour(self,col):
# #         self.col = col
# #     def show(self):
# #         print(f"颜色是{self.col}")
# #
# #
# # car_1 = Car();
# # car_1.colour("red")
# # car_1.show()
# #
# # car_2 = Car();
# # car_2.colour("blue")
# # car_2.show()
# # class Car:
# #     def __init__(self,wheels,colour):
# #         self.wheels =wheels
# #         self.colour = colour
# #
# #     def run(self):
# #         print(f"{self.wheels}个轮子的车，{self.colour}车在跑")
# # BWM = Car(4,'紅色')
# # BWM.run()
# # bmw = Car(4,'藍色')
# # bmw.run()
#
# # class A:
# #     def __init__(self):
# #         self._x = 10;
# #     def _foo(self):
# #         print("from")
# #     def bar(self):
# #         self._foo()
# #
# #
# # a = A()
# # print(a._x)
# # a._foo()
# # class Person:
# #     name = '人'
# #     age = 30
# #
# #     def speak(self):
# #         print(f"{self.name}今年{self.age}岁")
# #
# #
# #
# # class Stu(Person):
# #
# #     def set_name(selfself,newName):
# #         self.name = newName
# #     def s_speak(self):
# #         print(f"{self.name}今年{self.age}岁")
# #
# #
# # stu = Stu()
# # print(f"student的名字是{stu.name}")
# # class Sofa:
# #     def printA(self):
# #         print("这是沙发")
# #
# # class Bed:
# #     def printB(self):
# #         print("这是床")
# #
# #
# # class Sofabed(Sofa,Bed):
# #     def printC(self):
# #         print("这是沙发床")
# #
# #
# # obj_c = Sofabed()
# # obj_c.printA()
# # obj_c.printB()
# # obj_c.printC()
#
# # class Person:
# #     def __init__(self,name,sex):
# #         self.name = name
# #         self.sex =  sex
# #
# #
# # class Stu(Person):
# #     def __init__(self,name,sex,score):
# #         super().__init__(name,sex)
# #         self.score = score
# #
# # student = Stu('小王','男','100')
# # print(f"{student.name}的性别是{student.sex}，分数是{student.score}")
#
# class Person:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#     def who(self):
#         print(f"我是老师，我是{self.name}")
#
# class Stu(Person):
#     def __init__(self,name,gender,score):
#         super().__init__(name,gender)
#         self.score = score
#     def who(self):
#         print(f"我是学生，我是{self.name}")
#
#
# class Teacher(Person):
#     def __init__(self,name,gender,course):
#         super().__init__(name,gender)
#         self.scourse = course
#     def who(self):
#         print(f"我是老师，我是{self.name}")
#
#
# def fun(x):
#     x.who()
#
# p = Person('小王','男')
# s = Stu('小张','男',100)
# t = Teacher('小明','男','English')
#
#
# fun(p)
# fun(s)
# fun(t)

import os
from pathlib import Path
path = Path(r"d:\Users\21862\PycharmProjects\PythonProject\练习\pi.txt.txt")
os.chdir(r"d:\Users\21862\PycharmProjects\PythonProject\练习")
f = open(path,'w')