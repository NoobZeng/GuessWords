# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2019/9/10  6:13
# @Author : Noob
# @File   : demo_random.py

import random

# 1. 生成一个随机小数n，n大于等于0小于1.0
print("1. random.random()：生成一个随机小数n，n大于等于0小于1.0")
n = random.random()
print(n)

# 2. 生成一个指定范围内的小数，两个参数中一个是上限一个是下限
# 如果a<b，则生成的随机数n的范围在a<=n<=b
# 如果a>b，则生成的随机数n的范围在b<=n<=a
print("2. random.uniform(a, b)：生成一个指定范围内的小数，两个参数中一个是上限一个是下限")
n = random.uniform(10, 20)
print(n)
n = random.uniform(20, 15)
print(n)

# 3. 生成一个指定范围内的整数，其中参数a是下限，参数b是上限，生成的随机数范围在a<=n<=b
print("3. random.randint(a, b)：生成一个指定范围内的整数")
n = random.randint(5, 9)
print(n)

# 4. 从指定范围内按指定基数递增的集合中获取一个随机数（有点类似于有序列表的切片），start包含在范围内，stop不包含在范围内
print("4. random.randrange([start], stop[, step])：从指定范围内按指定基数递增的集合中获取一个随机数")
n = random.randrange(2, 10, 3)
print(n)

# 5. 重序列中获取一个随机元素，其原型为random.choice(sequence)，参数sequence标识一个有序类型。泛指序列数据结构，
# 字符串、列表、元祖都属于sequence。
print("5. random.choice(sequence)：从序列中获取一个随机元素")
n = random.choice("hello world")
print(n)
n = random.choice(("java", "C", "C++", "php"))
print(n)
n = random.choice(["java", "C", "C++", "php"])
print(n)

# 6. 打乱列表中的元素，shuffle()返回的是none，只是该函数改变了原列表数据的顺序
print("6. random.shuffle(x[, random)：打乱列表中的元素")
a = [1, 2, 3, 4, 5]
n = random.shuffle(a)
print(n)  # None
print(a)

# 7. 从指定序列中随机获取指定长度的片段，sample()函数不会修改原有序列
print("7. random.sample(sequence,k)：从指定序列中随机获取指定长度的片段")
a = "abcdefg"
n = random.sample(a, 3)
print(n)
print(a)