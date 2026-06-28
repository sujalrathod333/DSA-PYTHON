#160 intersection of two linked list



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):

        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA


# -------------------------
# Creating the common part
# -------------------------
common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

# List A: 4 -> 1 -> 8 -> 4 -> 5
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common

# List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common

# -------------------------
# Testing
# -------------------------
obj = Solution()
ans = obj.getIntersectionNode(headA, headB)

if ans:
    print("Intersection Node:", ans.val)
else:
    print("No Intersection")