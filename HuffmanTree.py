#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:11:12 2019

@author: adarsh
"""

import heapq
import math

class HuffmanTree:
    
    def __init__(self, string):
        self.root=None
        self.total=len(string)
        self.p_queue=self.init_queue(string)
        self.build_tree()
        self.code={}
        self.decode(self.root, '')
        self.string=string
        
    def init_queue(self, string):
        dic=self.count(string)
        qu=[]
        for i in dic:
            qu.append(Node(i,dic[i]))
        
        heapq.heapify(qu)
        print(qu)
        return qu
    
    def count(self, string):
        dic={}
        for i in string:
            if dic.get(i)==None:
                dic[i]=1
            else:
                dic[i]=dic[i]+1
        print(dic)
        return dic
    
    def build_tree(self):
        if self.root==None:
            self.add()
        while self.root.count!=self.total:
            self.add()        
    
    def add(self):
        n1=heapq.heappop(self.p_queue)
        n2=heapq.heappop(self.p_queue)
        node=Node(str(n1.name)+str(n2.name), n1.count+n2.count)
        node.left=n1
        node.right=n2
        self.root=node
        self.p_queue.append(node)
        print(self.p_queue)

    def decode(self, root, code):
        if root.left==None and root.right==None:
            self.code[root.name]=code
        else:
            self.decode(root.left, code+'0')
            self.decode(root.right, code+'1')
            
    def convert2code(self):
        s=''
        for i in self.string:
            s=s+self.code[i]
        return s
    
    def analyse(self):
        raw=math.ceil(math.log(len(self.code),2))*len(self.string)
        dic=self.count(self.string)
        coded=0
        for i in dic:
            coded=coded+dic[i]*len(self.code[i])
        
        print('Original Size : ', raw)
        print('Compressed Size : ', coded)
        print("Compression Fraction : ", coded/raw)
        

class Node:
    
    def __init__(self, nm, count):
        self.name=nm
        self.count=count
        self.right=None
        self.left=None
        
    def __gt__(self, node):
        return self.count>node.count
    
    def __lt__(self, node):

        return self.count<node.count
    
    def __repr__(self):
        return self.name+":"+str(self.count)
            

class HuffmanDecode:
    def  __init__(self, string, code):
        self.code=self.rev_dic(code)
        self.string=string 
        
    def rev_dic(self, code):
        dic={}
        for i in code:
            dic[code[i]]=i
        return dic
    
    def convert2str(self):
        s=''
        k=1
        i=0
        while i<len(self.string):
            
            while self.code.get(self.string[i:i+k])==None:
                k=k+1
            
            s=s+self.code[self.string[i:i+k]]
            i=i+k
            k=1
        return s
                
        
        
        
        
s='Plain text, Plain-text, or Plaintext is any text, text file, or document that contains only text. Unlike a rich-text document, a plain text file cannot have bold text, fonts, larger font sizes, or any other special text formatting. In the picture is a visual example of plain text vs. formatted text.Most associate plain text files with the file extension .txt on Microsoft Windows computers, however, can be any non-formatted file. To view a plaintext file, a text editor such as Microsoft Notepad is used. However, all text editors including Microsoft WordPad and Word can also be used to view plaintext files because they have no special formatting.'    
s=s+'Huffmans original algorithm is optimal for a symbol-by-symbol coding with a known input probability distribution, i.e., separately encoding unrelated symbols in such a data stream. However, it is not optimal when the symbol-by-symbol restriction is dropped, or when the probability mass functions are unknown. Also, if symbols are not independent and identically distributed, a single code may be insufficient for optimality. Other methods such as arithmetic coding often have better compression capability.Although both aforementioned methods can combine an arbitrary number of symbols for more efficient coding and generally adapt to the actual input statistics, arithmetic coding does so without significantly increasing its computational or algorithmic complexities (though the simplest version is slower and more complex than Huffman coding). Such flexibility is especially useful when input probabilities are not precisely known or vary significantly within the stream. However, Huffman coding is usually faster and arithmetic coding was historically a subject of some concern over patent issues. Thus many technologies have historically avoided arithmetic coding in favor of Huffman and other prefix coding techniques. As of mid-2010, the most commonly used techniques for this alternative to Huffman coding have passed into the public domain as the early patents have expired.For a set of symbols with a uniform probability distribution and a number of members which is a power of two, Huffman coding is equivalent to simple binary block encoding, e.g., ASCII coding. This reflects the fact that compression is not possible with such an input, no matter what the compression method, i.e., doing nothing to the data is the optimal thing to do.Huffman coding is optimal among all methods in any case where each input symbol is a known independent and identically distributed random variable having a probability that is dyadic, i.e., is the inverse of a power of two. Prefix codes, and thus Huffman coding in particular, tend to have inefficiency on small alphabets, where probabilities often fall between these optimal (dyadic) points. The worst case for Huffman coding can happen when the probability of the most likely symbol far exceeds 2−1 = 0.5, making the upper limit of inefficiency unbounded.There are two related approaches for getting around this particular inefficiency while still using Huffman coding. Combining a fixed number of symbols together ("blocking") often increases (and never decreases) compression. As the size of the block approaches infinity, Huffman coding theoretically approaches the entropy limit, i.e., optimal compression. However, blocking arbitrarily large groups of symbols is impractical, as the complexity of a Huffman code is linear in the number of possibilities to be encoded, a number that is exponential in the size of a block. This limits the amount of blocking that is done in practice.'  
    