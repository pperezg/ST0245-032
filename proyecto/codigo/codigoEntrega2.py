import sys
import pandas as pd
import timeit
import random

class Node:
    
    def __init__(self, ph, soil_temp, soil_moist, light, env_temp, env_humidity, label):
        self.left = None
        self.right = None
        self.parent = None
        self.ph = ph
        self.soil_temp = soil_temp
        self.soil_moist = soil_moist
        self.light = light
        self.env_temp = env_temp
        self.env_humidity = env_humidity
        self.label = label

class RedBlackTree():

    def __init__(self):
        self.EmptyT = Node(0,0,0,0,0,0,0)
        self.EmptyT.color = "Black"
        self.EmptyT.left = None
        self.EmptyT.right = None
        self.root = self.EmptyT

    def searchAux(self,node,light):
        if node == self.EmptyT or light==node.light:
            return ("Said value was found in the tree.")
        elif light < node.light:
            self.searchAux(node.left, light)
        else:
            self.searchAux(node.right, light)
    
    def helpDelete(self,node):
        while node != self.root and node.color=="Black":
            if node == node.parent.left:
                temp = x.parent.right
                if temp.color=="Red":
                    temp.color = "Black"
                    node.parent.color = "Red"
                    self.leftRotation(node.parent)
                    temp = node.parent.right
                if temp.left.color == "Black" and temp.right.color == "Black":
                    temp.color == "Red"
                    node = node.parent
                else:
                    if temp.right.color == "Black":
                        temp.left.color = "Black"
                        temp.color = "Red"
                        self.rightRotation(temp)
                    temp.color = node.parent.color
                    node.parent.color = "Black"
                    temp.right.color = "Black"
                    self.leftRotation(node.parent)
                    node = self.root
            else:
                temp = node.parent.left
                if temp.color == "Red":
                    temp.color = "Black"
                    node.parent.color = "Red"
                    self.rightRotation(node.parent)
                    temp = node.parent.left
                if temp.right.color == "Black" and temp.right.color == "Black":
                    temp.color = "Red"
                    node = node.parent
                else:
                    if temp.left.color == "Black":
                        temp.right.color = "Black"
                        temp.color = "Red"
                        self.leftRotation(temp)
                        temp = node.parent.left
                    temp.color = node.parent.color
                    node.parent.color = "Black"
                    temp.left.color = "Black"
                    self.rightRotation(node.parent)
                    node = self.root
        node.color = "Black"
    
    def redBlackTransplant(self, nodeone, nodetwo):
        if nodeone.parent == None:
            self.root = nodetwo
        elif nodeone == nodeone.parent.left:
            nodeone.parent.left = nodetwo
        else:
            nodeone.parent.right = nodetwo
        nodetwo.parent = nodeone.parent
    
    def deleteAux(self,node,light):
        z = self.EmptyT
        while node != self.EmptyT:
            if node.light == light:
                z = node
            if node.light <= light:
                node = node.right
            else:
                node = node.left
        if z == self.EmptyT:
            print ("Said light doesn't belong to any data.")
            return 
        y = z
        y_firstColor = y.color
        if z.left == self.EmptyT:
            x = z.right
            self.redBlackTransplant(z,z.right)
        elif (z.right == self.EmptyT):
            x = z.left
            self.redBlackTransplant(z,z.left)
        else:
            y = self.min(z.right)
            y_firstColor = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.redBlackTransplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.redBlackTransplant(z,y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_firstColor == "Black":
            self.helpDelete(x)

    def helpInsert(self,node):
        while node.parent.color == "Red":
            if node.parent == node.parent.parent.right:
                x = node.parent.parent.left
                if x.color == "Black":
                    x.color = "Red"
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rightRotation(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self.leftRotation(node.parent.parent)
            else:
                x = node.parent.parent.right
                if x.color=="Red":
                    x.color = "Black"
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.leftRotation(node)
                    k.parent.color = "Black"
                    k.parent.parent.color = "Red"
                    self.rightRotation(node.parent.parent)
            if node == self.root:
                break
        self.root.color = "Black"

    def search(self, light):
        return self.searchAux(self.root, light)
    
    def leftRotation(self, node):
        x = node.right
        node.right = x.left
        if x.left != self.EmptyT:
            x.left.parent = node
        x.parent = node.parent
        if node.parent == None:
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x
        x.left = node
        node.parent = x

    def rightRotation(self, node):
        x = node.left
        node.left = x.right
        if x.right != self.EmptyT:
            x.right.parent = node
        x.parent = node.parent
        if node.parent == None:
            self.root = x
        elif node == node.parent.right:
            node.parent.right = x
        else:
            node.parent.left = x
        x.right = node
        node.parent = x
        
    def delete(self, light):
        self.deleteAux(self.root,light)
        
    def min(self, node):
        while node.left != self.EmptyT:
            node = node.left
        return node

    def insert(self,  ph, soil_temp, soil_moist, light, env_temp, env_humidity, label):
        node = Node(ph, soil_temp, soil_moist, light, env_temp, env_humidity, label)
        node.parent = None
        node.light = light
        node.left = self.EmptyT
        node.right = self.EmptyT
        node.color = "Red"

        y = None
        x = self.root
        while x != self.EmptyT:
            y = x
            if node.light < x.light:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.light < y.light:
            y.left = node
        else:
            y.right = node
        if node.parent == None:
            node.color = 0
            return
        if node.parent.parent == None:
            return
        
dta = pd.read_csv("https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/DataSets/test/data_set_test.csv")
dta.head()
t = RedBlackTree()
for n in range(1,100):
    ph = dta.at[n,'ph']
    soilT = dta.at[n,'soil_temperature']
    soilM = dta.at[n,'soil_moisture']
    light = dta.at[n,'illuminance']
    envT = dta.at[n,'env_temperature']
    envH = dta.at[n,'env_humidity']
    lbl = dta.at[n,'label']
    t.insert(ph, soilT, soilM, light, envT, envH, lbl)
