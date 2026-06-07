class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):
    temp = head

    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next

    print("None")
    
def reorder(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        
    prev=None
    curr=slow.next
    slow.next=None
    
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
        
    first=head
    second=curr
    
    while second:
        t1=first.next
        t2=second.next
        first.next=second
        second.next=t1
        
        first=t1
        second=t2
    
    


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)

printList(reorder(l1))