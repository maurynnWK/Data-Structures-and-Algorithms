#Insertion can be done ata the beginning,in between two nodes and at the end of the linked list

#Inthe beginnning:
#Create a node
#Check if the head is pointing to any location
#if yes....point new node to the head which points to previous first node say B
#Delete value on head and point head to new node which is new node say A


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None#stores memory address of next 

class singlyLinkedList:        
    def __init__(self):
        self.head=None#initialize the head of
    def insertAtBeginning(self,data):   
       #create node
       node1=Node(data)

       #check if head is empty
       if self.head==None:
        self.head=node1
       else:
        #point newnode to the head
        node1.next=self.head

        #now value of head is changed to new node
        self.head=node1 
    
    def printList(self):
        node_to_read=self.head
        while node_to_read:
            print(node_to_read.data)
            node_to_read=node_to_read.next
        print("None")


mylist1=singlyLinkedList()

#call the insertAt beginning function to create node and insert at beginning
mylist1.insertAtBeginning("A")  
mylist1.insertAtBeginning("B")  
mylist1.insertAtBeginning("C")  
mylist1.insertAtBeginning("D")  
mylist1.insertAtBeginning("E")    
mylist1.printList()   