#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:41:01 2019

@author: adarsh
"""
import math
def SOE(n):
    if_prime=[0]*(n+1)
    prime=[]
    ul=int(math.sqrt(n+1))+1
    for i in range(2,ul):
        if if_prime[i]==0:
            prime.append(i)
            temp=i
            while temp<n+1:
                if_prime[temp]=1
                temp=temp+i
    for i in range(ul,n+1):
        if if_prime[i]==0:
            prime.append(i)
    return prime

import time

t1=time.time()
SOE(10000)
t2=time.time()
print('10000 iterations : ', t2-t1)
SOE(100000)
t3=time.time()
print('100000 iterations : ', t3-t2)
SOE(1000000)
t4=time.time()
print('1000000 iterations : ', t4-t3)



x=[]
y=[]

for i in range(1000, 1000000, 1000):
    t=time.time()
    SOE(i)
    t=time.time()-t
    x.append(i)
    y.append(t)
import matplotlib.pyplot as plt
plt.plot(x,y)
                
    