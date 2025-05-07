def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1) #Amount + 1 represents infinity as a placeholder
    dp[0] = 0 #Starting amount

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1

print(coinChange([1, 2, 5], 11))    #Output: 3 (5 + 5 + 1)
print(coinChange([2], 3))           #Output: -1 (Invalid)
print(coinChange([1], 0))           #Output: 0