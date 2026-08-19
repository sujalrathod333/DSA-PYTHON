#1047 Remove All Adjacent Duplicates In String
def removeDuplicates(s: str) -> str:
    stack = []

    for ch in s:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)


# Test case
s = "abbaca"

expected = "ca"
result = removeDuplicates(s)

print("Input:   ", s)
print("Expected:", expected)
print("Got:     ", result)

if result == expected:
    print("PASS")
else:
    print("FAIL")