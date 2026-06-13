def bestBuy(nums):
    minPrice=nums[0]
    profit=0
    for i in range(1, len(nums)):
        currProfit=nums[i]-minPrice
        if currProfit>profit:
         profit=currProfit
        minPrice=min(minPrice, nums[i])
    return profit


print(bestBuy([7,1,5,3,6,4]))
    