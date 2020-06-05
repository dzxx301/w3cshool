# -*- coding: utf-8 -*-
#  类访问限制举例
#  请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self._gender = gender

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        if (gender != 'male') and (gender != 'female'):
            raise ValueError('bad gender')
        else:
            self._gender = gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')