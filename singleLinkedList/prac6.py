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
                
    def deleteNth(self, head, n):
        dummy=Node(0)
        dummy.next=head
        slow=dummy
        fast=dummy
        
        for _ in range(n+1):
            fast=fast.next
        
        while fast:
          slow=slow.next
          fast=fast.next
          
        slow.next=slow.next.next
        
        return dummy.next
    
    def swapNode(self, head, k):
        first=head
        
        for _ in range(k-1):
            first=first.next
        
        fast=first
        second=head
        
        while fast.next:
            fast=fast.next
            second=second.next
            
        first.data, second.data= second.data, first.data
        
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
ll.head = ll.swapNode(ll.head, 2)
ll.printLinkedList()