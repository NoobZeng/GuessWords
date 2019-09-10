# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2019/9/10  22:16
# @Author : Noob
# @File   : test.py

import random

# 开始游戏
print(
    """
    欢迎参加猜单词游戏
    把字母组合成一个正确的单词
    """
)

# 判断游戏是否继续的标识
iscontinue = "y"
words = ["fiddler", "myeclipse", "pycharm", "sumblim", "jmeter", ""]
# 去掉单词库中的空字符串
# words = list(filter(None, words))

while iscontinue == "y" or iscontinue == "Y":
    # 判断词库列表长度
    if len(words) != 0:
        # 随机抽取一个单词
        word = random.choice(words)
        # 词库出现为空的单词就跳过
        if word == "" and len(words) != 1:
            continue
        elif word == "" and len(words) == 1:
            print("单词已经全部猜完，结束游戏！！！")
            break
        # random.sample(sequence, k)：随机获取指定长度的序列片段，得到的是一个数组，且不会修改到原序列
        # 通过join方法重新拼合成一个字符串，是乱序后的单词
        jumple = "".join(random.sample(word, len(word)))
        print("\n" + jumple)
        # 用于判断输入单词是否正确的标识
        correct = input("请输入该单词的正确拼写：")
        while correct != word:
            correct = input("猜错了，请思考后继续：")
        print("恭喜猜对了！！！")
        # 猜完后将该单词移出列表
        words.remove(word)
        if len(words) != 0:
            iscontinue = input("是否继续（Y/N）：")
    else:
        print("单词已经全部猜完，结束游戏！！！")
        break