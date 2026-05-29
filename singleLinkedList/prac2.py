class Node:
    def __init__(self, value):
        self.data = value
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def printLinkedList(self):
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
                
    def insertAt(self, value):
        newNode = Node(value)
        newNode.next= self.head
        self.head=newNode
        
    def insertLast(self, value):
        last=Node(value)
        
        temp=self.head
        
        while temp.next is not None:
            temp=temp.next
        temp.next=last
        
    def insertAtPos(self, value, pos):
        new = Node(value)
        
        if pos == 0:
            new.next=self.head
            self.head=new
            
        temp = self.head
        
        for i in range(pos - 1):
            temp=temp.next
        
        new.next=temp.next
        
        temp.next=new
        
    def deleteNode(self, value):
        temp = self.head
        
        if temp is not None and temp.data == value:
            self.head=temp.next
            return
        
        prev = None
        
        while temp is not None and temp.data != value:
            prev=temp
            temp=temp.next
            
        if temp is None:
            return
        
        prev.next=temp.next
            
    def search(self, key):
        temp = self.head
        
        while temp is not None:
            if temp.data == key:
                return True
            temp=temp.next
        return False
            
            
        
        
            
            
                
ll = LinkedList()

first=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)

first.next = second
second.next=third
third.next=fourth

ll.head= first

ll.insertAt(5)
ll.insertAt(6)
ll.insertLast(50)
print(ll.search(11))
ll.insertAtPos(11, 3)
print(ll.search(11))
