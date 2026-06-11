def largestAltitudes(gain):
    currAltitude = 0
    highest = 0
    for g in gain:
        currAltitude += g
        highest = max(highest, currAltitude)
    return highest

arr=[-9,1,5,-11,-9]
print(largestAltitudes(arr))