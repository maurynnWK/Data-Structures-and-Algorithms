#singly linked list-- we must use a class
# reate node class 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None#stores memory address of next 

node1=Node("A")
node2=Node("B")
node3=Node("C")

#memory adressess of object
# print(node1)
# print(node2)
print(node3)

#link the nodes together
node1.next=node2
node2.next=node3
#node3.next is None which is equal to null as it is the last node we have in the singly linked list

print(node2.next)
print(node1.next.next.data)
print(node2.data)