# create node class 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None#stores memory address of next


#singly linked list-- we must use a class
class Linked_List:
    def __init__(self):
        self.head=None

    # adding a node at the end of the linked list
    def append_list(self,data):
        newnode=Node(data)
        
        if self.head==None:
            self.head=newnode
            return
        else:
            current=self.head
            while current.next != None:
                current=current.next
            current.next=newnode

    #print list
    def  print_list(self):
        current=self.head
        while current:            
            print(current.data,end=" -> ")
            current=current.next

   ##getting length of the linked list\
    def find_length(self):
        length=0
        current=self.head
        while current:
            length+=1
            current=current.next
        print("Length of the linked list is:",length)

    def insert_begin(self,data):
        new_node=Node(data)
        to_shift=self.head
        self.head=new_node
        new_node.next=to_shift

    # def insert_middle(self,data,position):
    #     new_node=Node(data)
        
    #     if position== 0:
    #         self.insert_begin(data)
    #         return
        
    #     current=self.head
    #     count=0

    #     while current is not None and count<=position:
    #         current=current.next
    #         count+=1   

    #     to_shift=current   
    #     current.next=new_node
    #     new_node.next=to_shift
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_begin(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        # Go to node just before the target position
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range.")
            return

        new_node.next = current.next
        current.next = new_node

    

        
     




linked_list=Linked_List()
linked_list.append_list("A")
linked_list.append_list("B")
linked_list.append_list("D")
linked_list.append_list("E")
linked_list.append_list("F")



linked_list.print_list()
print()
linked_list.find_length()
linked_list.insert_begin("D")

linked_list.print_list()
print()
linked_list.find_length()
print()
linked_list.insert_middle("J",1)

print()
print()
linked_list.print_list()








# node1=Node("A")
# node2=Node("B")
# node3=Node("C")

# #memory adressess of object
# # print(node1)
# # print(node2)
# print(node3)

# #link the nodes together
# node1.next=node2
# node2.next=node3
# #node3.next is None which is equal to null as it is the last node we have in the singly linked list

# print(node2.next)
# print(node1.next.next.data)
# print(node2.data)