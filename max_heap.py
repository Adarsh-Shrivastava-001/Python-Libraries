#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:14:24 2019

@author: adarsh
"""

class MaxHeap:
    
    def __init__(self, arr):
        self.n=len(arr)
        self.heap=arr
        self.build_heap(arr)
        
    def parent(self, ind):
        if ind==0:
            return 0
        return (ind-1)//2
    
    def left(self, ind):
        if 2*ind+1>=self.n:
            return ind
        return 2*ind+1
    
    def right(self, ind):
        if 2*ind+2 >= self.n:
            return ind
        return 2*ind+2
        
    def build_heap(self, arr):
        for i in range(self.n):
            self.heapify(i)      
        
    def heapify(self, ind):
        if self.heap[ind]>self.heap[self.parent(ind)]:
            self.heap[ind],self.heap[self.parent(ind)]=self.heap[self.parent(ind)],self.heap[ind]
            self.heapify(self.parent(ind))
        
    def insert(self, ele):
        self.n=self.n+1
        self.heap.append(ele)
        self.heapify(self.n-1)
        print(self.heap)
        
    def pop(self):
        ele=self.heap[0]
        self.heap[0]=self.heap[self.n-1]   
        self.n=self.n-1
        self.rev_heapify(0)
        return ele
        
    def rev_heapify(self, ind):
        right=self.right(ind)
        left=self.left(ind)
        m=max(self.heap[ind], self.heap[left], self.heap[right])
        if m==self.heap[ind]:
            return
        elif m==self.heap[right]:
            self.heap[ind], self.heap[right]= self.heap[right], self.heap[ind]
            self.rev_heapify(right)
            
        elif m==self.heap[left]:
            self.heap[ind], self.heap[left]= self.heap[left], self.heap[ind]
            self.rev_heapify(left)
            
    def hsort(self):
        for i in range(self.n):
            print(self.pop())

import sys
sys.setrecursionlimit(70)
        
        