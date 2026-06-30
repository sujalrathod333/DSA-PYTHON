# backspace string compare


def checkData(s, t):
    s1=[]
    t1=[]
    
    for ch in s:
        if ch != '#':
            s1.append(ch)
        elif s1:
            s1.pop()
            
    for ch in t:
        if ch != '#':
            t1.append(ch)
        elif t1:
            t1.pop()
    
    
    return s1 == t1


s = "ab#c"
t = "ad#c"
 
print(checkData(s, t))