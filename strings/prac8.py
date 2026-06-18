def sorting(s):
    s1=list(sorted(s))
    return "".join(s1)

def groupAnagram(s):
    key={}
    for i in s:
      k=sorting(i)
      if k not in key:
          key[k] = []
      key[k].append(i)
    return list(key.values())



print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))