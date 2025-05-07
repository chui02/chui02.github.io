def divide(dividend: int, divisor: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:       #For overtflow cases
        return INT_MAX
    negative = (dividend < 0) != (divisor < 0)      #Finding the sign of result (negative, positive)
    dividend, divisor = abs(dividend), abs(divisor) #Convert to positive values w/ absolute value
    quotient = 0

    for i in range(31, -1, -1):     #Subtract divisor multiplied by the powers of 2
        if (dividend >> i) >= divisor:
            quotient += 1 << i
            dividend -= divisor << i
    return -quotient if negative else quotient

print(divide(10, 3))                #Output: 3
print(divide(7, -3))                #Output: -2
print(divide(-2147483648, -1))      #Output: 2147483647 for edge cases