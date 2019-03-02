#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:18:46 2019

@author: adarsh
"""

  
import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'




class Graph:
    
    def __init__(self,n,adj_mat, verbose=False):
        self.n=n
        self.e=0
        self.is_adj_mat=adj_mat
        self.__adj_mat=None
        self.__lin_list=None
        self.verbose=verbose
        if self.is_adj_mat==True:
            self.__adj_mat=[[0 for i in range(n)] for j in range(n)]
        else:
            self.__lin_list=[[] for i in range(n)]
            
        if verbose==True:
            self.actions=[]
            self.__edges=[]
            self.graph=nx.DiGraph()
            for i in range(n):
                self.graph.add_node(i)
            
            
        
    def add_edge(self, node1, node2, directed=True):
        
        if directed==True: 
            self.e=self.e+1
            if self.is_adj_mat==True:
                self.__adj_mat[node1][node2]=1
            else:
                self.__lin_list[node1].append(node2)
        else:
            self.e=self.e+2
            if self.is_adj_mat==True:
                self.__adj_mat[node1][node2]=1
                self.__adj_mat[node2][node2]=1
            else:
                self.__lin_list[node1].append(node2)
                self.__lin_list[node2].append(node1)
                
        if self.verbose==True:
            self.actions.append('Added edge : '+ str(node1)+'-'+str(node2))
            self.__edges.append([node1,node2])
            self.graph.add_edge(node1,node2)
            if directed==False:
                self.__edges.append([node2,node1])
                self.graph.add_edge(node2,node1)
                
            
            
    def connections(self, node):
        conn=[]
        if self.is_adj_mat==True:
            for i in range(self.n):
                if self.__adj_mat[node][i]==1:
                    conn.append(i)
        else:
            conn=self.__lin_list[node]
        
        return conn
                
    def bfs(self, node):
        qu=[node]
        visited=[0 for i in range(self.n)]
        visited[node]=1
        front=0
        
        while front < len(qu):
            neigh=self.connections(qu[front])
            for i in neigh:
                if visited[i]==0:
                    qu.append(i)
                    visited[i]=1
            print(qu[front])
            
            front=front + 1
            
    def dfs(self, node):
        stk=[node]
        visited=[0 for i in range(self.n)]
        visited[node]=1
        top=0
        print(node)
        
        
        while top>=0:
            neigh=self.connections(stk[top])
            if neigh==[]:
                top=top-1
            for i in neigh:
                f=0
                if visited[i]==0:
                    stk.append(i)
                    top=top+1
                    visited[i]=1
                    print(i)
                    f=1
                    break
                if f==0 and i==neigh[-1]:
                    top=top-1
                    
        
    def draw(self):
        return draw(a.graph)
             
                
        
a=Graph(10, 0, verbose=True)
a.add_edge(1,2,0)
a.add_edge(2,3,0)
a.add_edge(3,4,0)
a.add_edge(4,5,0)
a.add_edge(4,2,0)
a.add_edge(2,6,0)
a.add_edge(2,7,0)
a.add_edge(0,8,0)