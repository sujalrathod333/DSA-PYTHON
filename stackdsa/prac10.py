#921 minimum add to make paranthesis valid
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open=0
        answer=0
        for ch in s:
            if ch == '(':
                open+=1
            else:
                if open>0:
                    open-=1
                else:
                    answer+=1
        return open + answer