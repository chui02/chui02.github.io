def maxProfit(prices):
    if not prices: #For no profit case
        return 0

    buyLow = prices[0]
    sellHigh = 0

    for price in prices[1:]:
        if price < buyLow:
            buyLow = price
        else:
            sellHigh = max(sellHigh, price - buyLow)
    return sellHigh

print("Example 1:")
print(maxProfit([7,1,5,3,6,4]))     #Outputs: 5

print("Example 2:")
print(maxProfit([7,6,4,3,1]))       #Outputs: 0