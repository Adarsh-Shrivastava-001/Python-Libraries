#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:02:30 2019

@author: adarsh
"""

import math
import numpy as np

def cal_angle(pt1, pt2):
    num=pt2[1]-pt1[1]
    den=pt2[0]-pt1[0]
    if den==0:
        return math.degrees(math.pi/2)    
    else:
        ans=math.atan(num/den)
        if ans<0:
            return math.degrees((math.pi)+ans)
        elif ans==-0.0:
            return math.degrees(math.pi)
        return math.degrees(ans)


def check(arr):
    if len(arr)<3:
        return
    pt1=arr[-3]
    pt2=arr[-2]
    pt3=arr[-1]
    sign=(pt2[0]-pt1[0])*(pt3[1]-pt1[1])-(pt2[1]-pt1[1])*(pt3[0]-pt1[0])
    if sign>=0:
        return
    else:
        l=arr.pop()
        arr.pop()
        arr.append(l)
        check(arr)
    


def ConvexHull(arr):
    b_pt=[-1, 100000000]
    ind=None
    hull=[]
    l=len(arr)
    for i in range(l):
        if arr[i][1]<b_pt[1]:
            b_pt=arr[i]
            ind=i
    print('Bottom : ', b_pt)
    print('ind : ', ind)
    
    p_ang=[0]*l
    for i in range(l):
        if i==ind:
            p_ang[i]=1000
        else:
            p_ang[i]=cal_angle(b_pt, arr[i])
            
    inds=np.argsort(p_ang)
    print('inds : ', inds)
    print('p_ang : ', p_ang)
    
    hull.append(b_pt)
    hull.append(arr[inds[0]])
    
    for i in range(1,l-1):
        hull.append(arr[inds[i]])
        if len(hull)>=3:
            check(hull)
    return hull
        
        
    

pts=[[4,4],[4,0],[0,4],[0,0],[2,2],[1,2],[3,3],[3,5],[1,10]]
pts2=[[0, 3], [2, 2], [1, 1], [2, 1], 
                      [3, 0], [0, 0], [3, 3]]
hull=ConvexHull(pts2)
import matplotlib.pyplot as plt
plt.scatter(x=[i[0] for i in pts2], y=[i[1] for i in pts2])
plt.plot([i[0] for i in hull]+[hull[0][0]], [i[1] for i in hull]+[hull[0][1]], color='r')

plt.show()
    
            