# 61 rotate list
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=1
        dummy=head
        
        while dummy.next:
            dummy=dummy.next
            length+=1
        
        k = k % length
        if k ==0:
            return head
        
        curr=head
        
        i=1
        while i <= length - k - 1:
            curr=curr.next
            i +=1
            
        next_head=curr.next
        curr.next=None
        dummy.next=head
        
        return next_head
            
            
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


sol = Solution()
head = sol.rotateRight(head, 2)


curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")