#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:01:23 2019

@author: adarsh
"""
import math


class SegmentTree:
    def __init__(self, arr, app='sum'):
        self.n=len(arr)
        self.arr=arr
        self.size=2*(2**math.ceil(math.log(self.n,2)))-1
        self.tree=[0 for i in range(self.size)]
        self.kind=app
        if app=='sum':
            self.build(0,self.n-1)
        elif app=='max':
            self.build_max(0,self.n-1)
    
    def build(self, start, stop, ind=None):
        if ind==None:
            ind=0
        if start==stop:
            self.tree[ind]=self.arr[start]
            return self.arr[start]
        mid=int((start+stop)/2)
        self.tree[ind]=self.build(start,mid,2*ind+1)+self.build(mid+1,stop,2*ind+2)
        return self.tree[ind]
    
    def build_max(self, start, stop, ind=None):
        if ind==None:
            ind=0
        if start==stop:
            self.tree[ind]=self.arr[start]
            return self.arr[start]
        mid=int((start+stop)/2)
        self.tree[ind]=max(self.build_max(start,mid,2*ind+1),self.build_max(mid+1,stop,2*ind+2))
        return self.tree[ind]
    
    def range_sum(self, start, stop, l=None, r=None, ind=0):
        if l==None and r==None:
            l=0
            r=self.n-1
        if l>=start and r<=stop:
            return self.tree[ind]
        elif l>stop or r<start:
            return 0
        else:
            mid=int((l+r)/2)
            return self.range_sum(start,stop, l,mid, 2*ind+1)+self.range_sum(start,stop, mid+1,r, 2*ind+2)
        
    
    
    def range_max(self, start, stop, l=None, r=None, ind=0):
        if l==None and r==None:
            l=0
            r=self.n-1
        if l>=start and r<=stop:
            return self.tree[ind]
        elif l>stop or r<start:
            return 0
        else:
            mid=int((l+r)/2)
            return max(self.range_max(start,stop, l,mid, 2*ind+1),self.range_max(start,stop, mid+1,r, 2*ind+2))
        
    
        
    def range_inc(self,start, stop, inc_fac=1):
        for i in range(start, stop+1):
            self.arr[i]=self.arr[i]+inc_fac
        if self.kind=='sum':
            self.build(0,self.n-1,0)
        elif self.kind=='max':
            self.build_max(0,self.n-1,0)
        
    def ele_inc(self, ind, inc_fac, l=None, r=None, i=0):
        print(l,r,i)
        if l==None and r==None:
            l=0
            r=self.n-1
        if ind>=l and ind<=r:
            self.tree[i]+=inc_fac
        mid=int((l+r)/2)
        if l==r:
            return
        if ind>mid:
            self.ele_inc(ind, inc_fac,mid+1, r, i=2*i+2)
        else:
            self.ele_inc(ind, inc_fac,l ,mid, i=2*i+1)
        

        















