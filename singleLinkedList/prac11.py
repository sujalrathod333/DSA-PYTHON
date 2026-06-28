class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2

        carry = 0

        dummy = ListNode(0)
        curr = dummy

        while p1 or p2 or carry:

            total = carry

            if p1:
                total += p1.val
                p1 = p1.next

            if p2:
                total += p2.val
                p2 = p2.next

            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

        return dummy.next


def createLinkedList(arr):
    dummy = ListNode()
    curr = dummy

    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next


def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")



l1 = createLinkedList([2, 4, 3])
l2 = createLinkedList([5, 6, 4])

obj = Solution()

answer = obj.addTwoNumbers(l1, l2)

print("Result:")
printLinkedList(answer)