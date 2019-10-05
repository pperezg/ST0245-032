#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, name, size, author):
        self.sons = []
        self.parent = None
        self.name = name
        self.size = size
        self.author = author
    
class Tree():
    def __init__(self):
        self.root = None
          
    def add_file(self, name, size, author, location, node = None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(name, size, author)
        else:
            toBeAdded = Node(name, size, author)
            a = search(location)
            a.sons.append(toBeAdded)
            toBeAdded.parent = a
    
    def search(self, name):
        search_aux(name, self.root)
    
    def search_aux(self, name, actual):
        toBeReturned = None
        if actual==self.root and actual.name == name:
            toBeReturned = actual
        else:
            for n in range(0,len(actual.sons)):
                if actual.sons[n].name == name:
                    toBeReturned = actual.sons[n]
                else:
                    seach_aux(name, actual.sons[n])
        if  toBeReturned == None:
            print("No such file or directory")
        else:
            return toBeReturned
                    
    def findFilesByFolderAndSize(self, desiredSize, smallestSubfolder):
        a = search(smallestSubfolder)
        for p in range(0,len(a.sons)):
            if a.sons[p].size > desiredSize
                print (a.sons[p].name)
    
    def findFilesByFolderAndAuthor(self, desiredAuthor, smallestSubfolder):
        a = search(smallestSubfolder)
        for p in range(0,len(a.sons)):
            if a.sons[p].author > desiredAuthor
                print (a.sons[p].name)
    
    def findInDirectory(self, smallestSubfolder):
        a = search(smallestSubfolder)
        for p in range(0,len(a.sons)):
            print (a.sons[p].name)
            
    def printOnTXT(self, act=None):
        if act==None:
            act = self.root
        f= open("fileDirectory.txt","w+")
        while len(act.sons)!=0:
            for p in range (0, len(act.sons)):
                print("├── ["act.sons[p].author+" "+act.sons[p].size+"K] "+act.sons[p].name)
                printOnTXT(self, act.sons[p])

