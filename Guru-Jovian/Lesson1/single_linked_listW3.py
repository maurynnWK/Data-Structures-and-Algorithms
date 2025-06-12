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

    ## adding a node at a certain position of the linked list
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_begin(data)
            return

        new_node = Node(data)
        current = self.head
        count = 1

        # Go to node just before the target position
        while current != None and count < position:
            current = current.next
            count += 1

        to_shift=current.next
        current.next=new_node
        new_node.next=to_shift
    
    #traverse the linked list
    def traverse(self):
        current=self.head
        while current !=None:
            print(current.data,end="->")
            current=current.next

    #delete an item
    def delete_item(self,item):
        current=self.head
        while current != None:
            if current.next.data==item:
                current=current.next.next

     




linked_list=Linked_List()
linked_list.append_list("A")
linked_list.append_list("B")
linked_list.append_list("D")
linked_list.append_list("E")
linked_list.append_list("F")



# linked_list.traverse()
# print()
# linked_list.find_length()
# linked_list.insert_begin("D")

# linked_list.traverse()
# print()
# linked_list.find_length()
# print()
# linked_list.insert_at_position("J",2)
# print()
# linked_list.traverse()
# print()
# print()
linked_list.delete_item("B")
linked_list.traverse()






