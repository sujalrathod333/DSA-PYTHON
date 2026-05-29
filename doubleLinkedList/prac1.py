class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
        self.prev=None
        
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    
    def insertAtBegining(self, value):
        newNode=Node(value)
        
        temp=self.head
        if temp is not None:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
        
    def insertAtLast(self, value):
        newNode=Node(value)
        
        if self.head is None:
          self.head = newNode
          return
    
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newNode
        newNode.prev=temp
    
    def instertAtPos(self, value, pos):
        newNode=Node(value)
        
        
        if pos==1:
            newNode.next=self.head
            if self.head is not None:
                self.head.prev=newNode
            self.head=newNode
            return
        
        temp=self.head
        
        for i in range(pos-2):
           if temp is not None:
               temp=temp.next
           if temp is None:
               return
           
        newNode.next=temp.next
           
        if temp.next is not None:
         temp.next.prev=newNode
               
        temp.next=newNode
        newNode.prev=temp
    
    def deleteNode(self):
        if self.head is None:
          return
    
        temp=self.head
        
        while temp.next is not None:
            temp=temp.next
            
        if temp.prev is not None:
                temp.prev.next= None
        else:
                self.head=None
            

dll=DoubleLinkedList()

first=Node(10)
second=Node(20)
third=Node(30)

dll.head=first
first.next=second
second.prev=first
second.next=third
third.prev=second

dll.insertAtBegining(50)
dll.insertAtLast(60)
dll.instertAtPos(14,2)
dll.deleteNode()
dll.printList()