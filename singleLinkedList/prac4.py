class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def cycle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:

            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)


l1.next.next.next = l1.next.next

ans = cycle(l1)

if ans:
    print("Cycle starts at:", ans.val)
else:
    print("No Cycle")