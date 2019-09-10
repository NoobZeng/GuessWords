# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2019/9/10  6:13
# @Author : Noob
# @File   : demo_slice.py

# python中符合序列的有序序列都支持切片（slice）
# 如：字符串、列表（list）、元祖（tuple）
# 格式：[start: end: step]
# start：起始索引，从0开始，-1表示结束
# end：结束索引，切片结果不包含结束索引，即不包含最后一位，-1代表最后一个位置索引
# step：步长，可以不提供，默认值是1，但是值不能为0，不然会报错ValueError: slice step cannot be zero
# end-start=正数时，从左向右取值，end-start=负数时，反向取值

"""
举例：字符串
"""
str_slice = "python"

print("1. 全部截取")
str1 = str_slice[:]
print(str1)
# python

print("2. 从0开始到3，每次增加1截取，不包含索引结束的位置")
str2 = str_slice[0: 3: 1]
print(str2)
# pyt

print("3. 从0到倒数第二位，每次增加2截取，不包含索引结束的位置")
str3 = str_slice[0: -1: 2]
print(str3)
# pto

print("4. 默认从起始位置索引，每次增加1截取，结束索引为3，省略步长")
str4 = str_slice[: 3]
print(str4)
# pyt

print("5. 反向取值，每次增加1截取，不包含索引结束位置")
str5 = str_slice[3: 0: -1]
print(str5)
# hty

print("6. 从索引3开始到结束索引，省略步长1")
str6 = str_slice[3:]
print(str6)
# hon