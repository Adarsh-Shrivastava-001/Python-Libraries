#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:48:07 2019

@author: adarsh
"""
import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


class Tree:    
    def __init__(self, arr=None):
        self.root=None
        self.diagram=nx.Graph()
        if arr==None:
            self.container=[]
        else:
            self.container=arr
            for i in self.container:
                self.add_node(i, self.root)
            
    def add_node(self, val, root=None):
        if root==None:
            root=self.root     
        if self.root==None:
            self.root=Node(val)
           
        else:
            if val>root.val:
                nex=root.right
                if nex==None:
                    root.right=Node(val)
                    self.diagram.add_edge(root, root.right)                    
                else:
                    self.add_node(val,nex)
                    
            else:
                nex=root.left
                if nex==None:
                    root.left=Node(val)
                    self.diagram.add_edge(root, root.left)
                else:
                    self.add_node(val,nex)
                    
    def inorder(self, root='null'):
        if root=='null':
            root=self.root
        
        if root==None:
            return

        self.inorder(root.left)
        print(root)
        self.inorder(root.right)
            
             
    def preorder(self, root='null'):
        if root=='null':
            root=self.root
        if root==None:
            return
        print(root)
        self.preorder(root.left)
        self.preorder(root.right)
        
    def least(self, root='null'):
        if root=='null':
            root=self.root
        if root.left==None:
            return root
        else:
            return self.least(root.left)
            
    def largest(self, root='null'):
        if root=='null':
            root=self.root
            
        if root.right==None:
            return root
        else:
            return self.largest(root.right)
            
    def draw(self):
        return draw(self.diagram)
    
    def search(self, val, root='null'):
        if root=='null':
            root=self.root
        if root==None:
            return -1
        if val==root.val:
            return root
        elif val>root.val:
            return self.search(val,root.right)
        else:
            return self.search(val,root.left)
            
            
        
    def delete(self, val):
        node=self.search(val)
        new_val=self.largest(node.left)
        self.diagram.remove_node(new_val)
        node.val=new_val.val        
        new_val.val=None
        
            
        
        
    def test(self):
        w=self.root.right
        return w
        
        
    
class Node:
    
    def __init__(self, val=None):
        self.val=val
        self.left=None
        self.right=None
        
    def __repr__(self):
        return str(self.val)
    
