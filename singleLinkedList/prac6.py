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
                
    def deleteMiddle(self, head):
        if not head.next:
            return None
        
        slow=head
        prev=None
        fast=head
        
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
            
            
        prev.next=slow.next
        return head    
                
ll = LinkedList()

first=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)
fifth=Node(50)
sixth=Node(60)
seventh=Node(70)



first.next = second
second.next=third
third.next=fourth
fourth.next=fifth
fifth.next=sixth
sixth.next=seventh
seventh.next=None

ll.head= first

# ll.printLinkedList()
ll.head = ll.deleteMiddle(ll.head)
ll.printLinkedList()