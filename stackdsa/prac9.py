#1021 Remoive Outermost Parenthesis
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        depth = 0
        for ch in s:
            if ch == "(":
                if depth > 0:
                 stack.append(ch)
                depth +=1
            else:
                if ch == ")":
                    depth -=1
                    if depth > 0:
                     stack.append(ch)
        return "".join(stack)
