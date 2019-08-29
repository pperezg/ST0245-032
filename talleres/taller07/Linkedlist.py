class nodo:
    def __init__(self,data):
        self.dato = data
        self.nextData = null

class Linkedlist:
    def __init_(self):
        self.firstElement = null
        self.size = 0

    def insert_at_the_beggining(self, e):
        temp = nodo(e)
        temp.nextNode=self.firstElement
        firstElement = temp
        self.size = self.size + 1

    def get_in_place(self, i):
        temp = self.firstElement
        for n in range(1, n <= i):
            temp = self.nextData
        return temp

    def insert_at_N(node, n, data):
        if n==0:
            insert_at_the_beggining(data)
        else:
            temp = node(data)
            the_one_before = get_in_place(n-1)
            temp.nextData = the_one_before.nextData
            the_one_before.nextData = temp # Complexity O(n);

    def delete_at_the_begging(self):
        self.firstElement = get_in_place(1)
        self.size = self.size - 1

    def delete_in_place(self, j):
        if j == 0:
            return delete_at_the_begging(self)
        else:
            get_in_place(j - 1).nextNode = get_in_place(j + 1)
            self.size = self.size - 1
            
    def search_value(self, k):
        temp = self.firstElement
        if temp == k:
            return 0
        i = 1
        while temp.nextNode != null:
            if temp.nextNode == k:
                return i
            i = i + 1
            temp = temp.nextNode
        return -1
