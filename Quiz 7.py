def coin(n: int) -> int:
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        total = mid * (mid + 1) // 2
        if total == n:
            return mid
        elif total < n:
            left = mid + 1
        else:
            right = mid - 1
    return right

print(coin(5))
print(coin(8))