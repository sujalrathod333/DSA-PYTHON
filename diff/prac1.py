class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(n):
            total=0
            while n:
                digit=n%10
                total+=digit**2
                n//=10
            return total
            
        slow=n
        fast=n
            
        while True:
            slow=squareSum(slow)
            fast=squareSum(squareSum(fast))
            if slow == fast:
               break
        return slow==1

num=Solution()
result=num.isHappy(19)
print(result)