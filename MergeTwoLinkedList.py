

class Node:
    def __init__(self):
        self.data=None
        self.next=None
    
    def setData(self,data):
        self.data=data
    
    def setNext(self,next):
        self.next=next
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertNode(self,data):
        node=Node()
        node.setData(data)
        if self.head is None:
            self.head=node
            return
        node2=self.head
        while node2.getNext() is not None:
            node2=node2.getNext()
        node2.setNext(node)
    
    def insertFinalNode(self,data):
        node=Node()
        node.setData(data)
        node2=self.head
        if self.head is None:
            self.head=node
            return
        else:
            node.setNext(node2)
            self.head=node
    
    def display(self):
        node=self.head
        if node is None:
            print("Underflow")
        else:
            while node is not None:
                print(node.getData(),end=' ')
                node=node.getNext()
        print()

L1=LinkedList()
L2=LinkedList()
L3=LinkedList()

n=input()
N=n.split()
a=0
A=list()
for i in N:
    A.append(int(i))
while A[a]!=-1:
    L1.insertNode(A[a])
    a+=1

m=input()
M=m.split()
b=0
B=list()
for j in M:
    B.append(int(j))

while B[b]!=-1:
    L2.insertNode(B[b])
    b+=1



firstNode=L1.head

secondNode=L2.head


while firstNode is not None:
    if secondNode is not None:
        if firstNode.getData() < secondNode.getData():
            L3.insertFinalNode(firstNode.getData())
            firstNode=firstNode.getNext()
        else:
            L3.insertFinalNode(secondNode.getData())
            secondNode=secondNode.getNext()
        continue
    while firstNode is not None:
        L3.insertFinalNode(firstNode.getData())
        firstNode=firstNode.getNext()
while secondNode is not None:
    L3.insertFinalNode(secondNode.getData())
    secondNode=secondNode.getNext()


"""while firstNode is not None:
    L3.insertFinalNode(firstNode.getData())
    firstNode=firstNode.getNext()

secondNode=L2.head

while secondNode is not None:
    L3.insertFinalNode(secondNode.getData())
    secondNode=secondNode.getNext()"""

L3.display()
