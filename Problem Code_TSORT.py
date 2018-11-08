# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:17:21 2018

@author: sonau
"""
num=[]
for i in range(int(input())):
    n=int(input())
    num.append(n)
num=sorted(num)
for i in num:
    print(i)
