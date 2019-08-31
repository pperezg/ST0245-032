import numpy

class ArrayList():

    def __init__(self):
        self.defaultSize = 10
        self.actualSize = self.defaultSize
        self.__elements = numpy.empty(self.actualSize, dtype=object)
        self.size = 0

    def size(self):
        return self.size

    def extend(self):
        self.actualSize = self.actualSize * 2
        elements2 = numpy.empty(self.actualSize, dtype=object)
        for n in range (1,self.size+1):
            elements2[n] = self.__elements[n]
            self.__elements = elements2;

    def get(self, index):
        return self.__elements[index]

    def add(self, object):
        if (self.size<self.actualSize):
            self.__elements[self.size+1] = object
            self.size = self.size+1
        else:
            self.extend()
            self.__elements[self.size+1]
            self.size = self.size+1

    def addInIndex(self, index, object):
        if (self.size==self.actualSize):
            self.extend()
            for n in range (self.size+1, index-1, -1):
                self.__elements[n] = self.__elements[n-1]
            self.elements[index] = object
            self.size = self.size+1
        else:
            for n in range (self.size+1, index-1, -1):
                self.__elements[n] = self.__elements[n-1]
            self.elements[index] = object
            self.size = self.size+1

arr = ArrayList()
arr.add(23)
print (arr.get(1))
