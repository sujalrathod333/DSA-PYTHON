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


def palindrome(head):
    slow = head
    fast = head

    # Find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None

    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Compare
    left = head
    right = prev

    while right:
        if left.val != right.val:
            return False

        left = left.next
        right = right.next

    return True


def palindrom1(head):
    vals=[]
    curr=head
    
    while curr:
        vals.append(curr.val)
        curr=curr.next
    return vals==vals[::-1]

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(1)

printList(l1)
print(palindrom1(l1))