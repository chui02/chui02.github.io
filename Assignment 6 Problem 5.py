def pow(x: float, n: int) -> float:
    def sol(base, exponent):
        if exponent == 0:
            return 1
        half = sol(base, exponent // 2)
        if exponent % 2 == 0:
            return half * half
        else:
            return half * half * base

    if n < 0:
        x = 1 / x
        n = -n
    return sol(x, n)

print(pow(2.00000, 10)) #1024.0
print(pow(2.10000, 3))  #9.261
print(pow(2.00000, -2)) #0.25