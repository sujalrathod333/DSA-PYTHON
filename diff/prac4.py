
def countOdds( low, high):
        count=0
        for i in range(low, high +1):
            if i % 2 !=0:
                count+=1
        return count

print(countOdds(3, 8))