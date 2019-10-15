#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import json
import random

'''
def facto(x):
    if (x == 0):
        return 1
    elif (x == 1):
        return 1
    else:
        return x * facto(x - 1)


def comb(n, i):
    return (facto(n) / facto(i) / facto(n - i))


Sanpai_Weight_1 = []  # 散牌出现在前墩时各种牌面的权值，按最大牌算权值，前墩最小权值对应的牌为5
Sanpai_Weight_2 = []  # 散牌出现在中墩是各种牌面的权值，按最大牌算权值，中墩最小权值对应的牌为7
# 不可能出现后墩是散牌的情况

Duizi_Weight_1 = []  # 对子出现在前墩时各种牌面的权值，按对子牌面算权值
Duizi_Weight_2 = []  # 对子出现在中墩时各种牌面的权值，按对子牌面算权值
Duizi_Weight_3 = []  # 对子出现在后墩时各种牌面的权值，按对子牌面算权值

Erdui_Weight_2 = []  # 对子出现在中墩时各种牌面的权值，按对子牌面算权值
Erdui_Weight_3 = []  # 对子出现在后墩时各种牌面的权值，按对子牌面算权值

Liandui_Weight_2 = []  # 连对出现在中墩时各种牌面的权值，按对子牌面算权值
Liandui_Weight_3 = []  # 连对出现在后墩时各种牌面的权值，按对子牌面算权值

Santiao_Weight_1 = []  # 三条出现在前墩时各种牌面的权值，按三条牌面算权值
Santiao_Weight_2 = []  # 三条出现在中墩时各种牌面的权值，按三条牌面算权值
Santiao_Weight_3 = []  # 三条出现在后墩时各种牌面的权值，按三条牌面算权值

Shunzi_Weight_2 = []  # 顺子出现在中墩时各种牌面的权值，按最大牌面算权值
Shunzi_Weight_3 = []  # 顺子出现在后墩时各种牌面的权值，按最大牌面算权值

Tonghua_Weight_2 = []  # 同花出现在中墩时各种牌面的权值，按最大牌面算权值
Tonghua_Weight_3 = []  # 同花出现在后墩时各种牌面的权值，按最大牌面算权值

Hulu_Weight_2 = []  # 葫芦出现在中墩时各种牌面的权值，按其中三条的值算权值
Hulu_Weight_3 = []  # 葫芦出现在后墩时各种牌面的权值，按其中三条的值算权值

Zhadan_Weight_2 = []  # 炸弹出现在后墩时各种牌面的权值，按炸弹的大小算权值
Zhadan_Weight_3 = []  # 炸弹出现在后墩时各种牌面的权值，按炸弹的大小算权值

Tonghuashun_Weight_2 = []  # 同花顺出现在中墩时各种牌面的权值，按最大牌的大小算权值
Tonghuashun_Weight_3 = []  # 同花顺出现在后墩时各种牌面的权值，按最大牌的大小算权值

Sanpai_Weight_1 = [0, 0, 0, 0, 0]
count = 0
for i in range(2, 12):
    count += 64 * comb(i, 2)
    weight = int(count / 22100 * 10000)
    Sanpai_Weight_1.append(weight)
print("前墩杂牌")
print(Sanpai_Weight_1)
Duizi_Weight_1 = [0, 0, ]
count = 18304
for i in range(13):
    weight = int(count / 22100 * 10000)
    Duizi_Weight_1.append(weight)
    count += 288
print("前墩对子")
print(Duizi_Weight_1)
Santiao_Weight_1 = [0, 0, ]
count = 18304 + 3744
for i in range(13):
    weight = int(count / 22100 * 5000)
    Santiao_Weight_1.append(weight)
    count += 4
print("前墩三条")
print(Santiao_Weight_1)
Sanpai_Weight_2 = [0, 0, 0, 0, 0, 0, 0, ]

print("中墩")
count = 0
for i in range(7, 15):
    weight = int(count / 2598960 * 100000)
    Sanpai_Weight_2.append(weight)
    count += (1024 * comb(i - 2, 4) - 1024 - 4 * comb(i - 2, 4) + 4)
print(count)
print(Sanpai_Weight_2)
count=0
Duizi_Weight_2 = [0, 0, ]
for i in range(2, 15):
    weight = int(count / 1098240 * 8100+1400)
    Duizi_Weight_2.append(weight)
    count += 6 * comb(12, 3) * 64
print(count)
print(Duizi_Weight_2)
count=0
Erdui_Weight_2 = [0, 0, 0, 0]
for i in range(4, 15):
    weight = int(count / 197160 * 90000+10000)
    Erdui_Weight_2.append(weight)
    count += 36 * (i - 3) * 44
print(count)
print(Erdui_Weight_2)

Liandui_Weight_2 = [0, 0, 0, ]
for i in range(3, 15):
    weight = int(count / 197160 * 90000+10000)
    Liandui_Weight_2.append(weight)
    count += 36 * 44
print(count)
print(Liandui_Weight_2)

Sanpai_Weight_2 = [0, 0, ]
for i in range(2, 15):
    weight = int(count / 197160 * 90000+10000)
    Sanpai_Weight_2.append(weight)
    count += 4 * comb(12, 2) * 16
print(count)
print(Sanpai_Weight_2)

Shunzi_Weight_2 = [0, 0, 0, 0, 0, 0]
for i in range(6, 15):
    weight = int(count / 197160 * 90000+10000)
    Shunzi_Weight_2.append(weight)
    count += 1020
print(count)
print(Shunzi_Weight_2)

Tonghua_Weight_2 = [0, 0, 0, 0, 0, 0, 0]
for i in range(7, 15):
    weight = int(count / 197160 * 90000+10000)
    Tonghua_Weight_2.append(weight)
    count += 4 * comb(i - 2, 4) - 4
print(count)
print(Tonghua_Weight_2)

Hulu_Weight_2 = [0, 0, ]
for i in range(2, 15):
    weight = int(count / 197160 * 90000+10000)
    Hulu_Weight_2.append(weight)
    count += 4 * 6 * 12
print(count)
print(Hulu_Weight_2)

Zhadan_Weight_2 = [0, 0, ]
for i in range(2, 15):
    weight = int(count / 197160 * 90000+10000)
    Zhadan_Weight_2.append(weight)
    count += 48
print(count)
print(Zhadan_Weight_2)

Tonghuashun_Weight_2 = [0, 0, 0, 0, 0, 0]
for i in range(6, 15):
    weight = int(count / 197160 * 90000+10000)
    Tonghuashun_Weight_2.append(weight)
    count += 4
print(count)
print(Tonghuashun_Weight_2)

print("后墩")

count = 0
Duizi_Weight_2 = [0, 0, ]
for i in range(2, 15):
    weight = int(count / 1295400 * 100000)
    Duizi_Weight_2.append(weight)
    count += 6 * comb(12, 3) * 64
print(count)
print(Duizi_Weight_2)

Erdui_Weight_2 = [0, 0, 0, 0]
for i in range(4, 15):
    weight = int(count / 197160 * 99000+1000)
    Erdui_Weight_2.append(weight)
    count += 36 * (i - 3) * 44
print(count)
print(Erdui_Weight_2)

Liandui_Weight_2 = [0, 0, 0, ]
for i in range(3, 15):
    weight = int(count / 197160 * 99000+1000)
    Liandui_Weight_2.append(weight)
    count += 36 * 44
print(count)
print(Liandui_Weight_2)

Sanpai_Weight_2 = [0, 0, ]
for i in range(2, 15):
    weight = int(count / 197160 * 99000+1000)
    Sanpai_Weight_2.append(weight)
    count += 4 * comb(12, 2) * 16
print(count)
print(Sanpai_Weight_2)

Shunzi_Weight_2 = [0, 0, 0, 0, 0, 0]
for i in range(6, 15):
    weight = int(count / 197160 * 99000+1000)
    Shunzi_Weight_2.append(weight)
    count += 1020
print(count)
print(Shunzi_Weight_2)

Tonghua_Weight_2 = [0, 0, 0, 0, 0, 0, 0]
for i in range(7, 15):
    weight = int(count / 197160 * 99000+1000)
    Tonghua_Weight_2.append(weight)
    count += 4 * comb(i - 2, 4) - 4
print(count)
print(Tonghua_Weight_2)

Hulu_Weight_2 = [0, 0, ]
for i in range(2, 15):
    weight = int(count / 197160 * 99000+1000)
    Hulu_Weight_2.append(weight)
    count += 4 * 6 * 12
print(count)
print(Hulu_Weight_2)

Zhadan_Weight_2 = [0, 0, ]
for i in range(2, 15):
    weight = int(count / 197160 * 99000+1000)
    Zhadan_Weight_2.append(weight)
    count += 48
print(count)
print(Zhadan_Weight_2)

Tonghuashun_Weight_2 = [0, 0, 0, 0, 0, 0]
for i in range(6, 15):
    weight = int(count / 197160 * 99000+1000)
    Tonghuashun_Weight_2.append(weight)
    count += 4
print(count)
print(Tonghuashun_Weight_2)

'''
while (True):
    list = [x for x in range(52)]

    cards = ["*A", "$A", "&A", "#A",
             "*2", "$2", "&2", "#2",
             "*3", "$3", "&3", "#3",
             "*4", "$4", "&4", "#4",
             "*5", "$5", "&5", "#5",
             "*6", "$6", "&6", "#6",
             "*7", "$7", "&7", "#7",
             "*8", "$8", "&8", "#8",
             "*9", "$9", "&9", "#9",
             "*10", "$10", "&10", "#10",
             "*J", "$J", "&J", "#J",
             "*Q", "$Q", "&Q", "#Q",
             "*K", "$K", "&K", "#K", ]
    numbers = random.sample(list, 13)
    str_data = ""
    for i in numbers:
        str_data = str_data + cards[i] + " "
    str_data = str_data[0:len(str_data) - 1]
    data = {
        "card": str_data
    }
    json.dumps(data)
    res = requests.post('http://172.26.76.171:7777/getcards', data)
    print(res.json())