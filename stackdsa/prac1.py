def valid(s):
    st=[]
    
    map={
        ')': '(',
        '}': '{',
        "]": "["
    }
    
    for ch in s:
        if ch in "({[":
            st.append(ch)
        else:
            if not st:
                return False
            top = st.pop()
            
            if top != map[ch]:
                return False
    return len(st) == 0
    
    
s = "()[]{}"

print(valid(s))
            