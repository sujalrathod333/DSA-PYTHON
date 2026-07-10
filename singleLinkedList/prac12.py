#23 merge k sorted lists


def __repr__(self):
      
        vals = []
        node = self
        while node:
            vals.append(str(node.val))
            node = node.next
        return " -> ".join(vals) if vals else "None"
 
 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0  
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
 
        dummy = ListNode(-1)  
        tail = dummy           
       
        while heap:
            val, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
 
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
 
        return dummy.next