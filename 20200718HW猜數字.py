#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 10:25:33 2020

@author: zhengs
"""


import random
ans = random.randint(0,20)
Time = 0
while Time<5: 
    guess = int(input('請在1~20之間，猜一個數字: '))
    Time=Time+1
    if guess<0 or guess>20:
        print ('輸入錯誤！')
    else:
        if guess==ans:
            print('答對了欸！好棒棒喔～')
            print ('你猜了',Time,'次')
            break
        elif guess>ans:
            print ("小一點喔～")
        elif guess<ans:
            print ("大一點啦～")
   
            
            
    



