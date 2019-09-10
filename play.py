# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2019/9/10  3:51
# @Author : Noob
# @File   : play.py

# 导入random模块
import random

# 创建单词序列
words = ("python", "java", "peal", "vue", "http", "javascript", "php", "cplus")

# 开始游戏
print(
    """
    欢迎参加猜单词游戏
    把字母组合成一个正确的单词
    """
)

iscontinue = "y"

while iscontinue == 'y' or iscontinue == 'Y':
    # 从序列中随机抽出一个单词
    word = random.choice(words)
    # 一个用于判断玩家是否才对的变量
    correct = word
    # 创建乱序后单词
    jumble = ""
    while word:  # word不是空串循环
        # 根据word长度产生word的随机位置
        position = random.randrange(len(word))
        # 将position位置的字母组合到乱象需后单词
        jumble += word[position]
        # 通过切片将position位置的字母从元单词中
        word = word[:position] + word[(position+1):]
    print("乱序后单词：", jumble)

    guess = input("\n请你猜：")
    while (guess != correct and guess != "") or (guess == ""):
        print("对不起不正确.")
        guess = input("继续猜：")
    if guess == correct:
        print("真棒，你猜对了！")
    iscontinue = input("\n是否继续（Y/N)：")