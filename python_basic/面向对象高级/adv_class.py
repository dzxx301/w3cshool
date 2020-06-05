# -*- coding: utf-8 -*-

#  1.使用___slots__
# class Student(object):
#     __slots__ = ('name','age')    # 用tuple定义允许的属性
#
# s = Student()
# s.name ='Michael'
# s.age  = 25
# #  s.score= 99  绑定score属性出错
# print(s.name)
# print(s.age)

#  2.使用@property和装饰器
class Screen(object):
                        # Python内置的@property装饰器就是负责把一个方法变成属性调用的：
    @property           # getter方法
    def width(self):            # 方法变属性
        return self._width

    @width.setter               # setter方法
    def width(self,value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0:
            raise ValueError('width must > 0!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if not isinstance(value, int):    #  判断量是否是对应数据类型
            raise ValueError('height must be an integer!')
        if value < 0:
            raise ValueError('height must > 0!')
        self._height = value

    @property       # 只有setter，没有setter，表示只读属性
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height= 768
print('resolution =',s.resolution)
if s.resolution == 786432:
    print('测试通过')
else:
    print('测试失败')