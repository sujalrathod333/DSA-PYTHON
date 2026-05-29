class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
        
        
first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
head=first

first.next = second
second.next = fourth
fourth.next = third

new = Node(5)
new.next=head
head=new

last = Node(50)
temp = head
while temp.next is not None:
    temp = temp.next
temp.next=last

temp=head
while temp is not None:
    print(temp.data)
    temp=temp.next
    
    