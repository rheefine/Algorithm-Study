# 시간 복잡도: O(sqrt(n))
def solution1(n):
    i = 0
    while (i * i <= n):
        if i * i == n:
            return 1
        i += 1
    return 0

# retry
# 시간 복잡도: O(logN)
def solution2(n):
    l = 0
    r = n
    while (l <= r):
        mid = (l + r) // 2
        if mid * mid == n:
            return 1
        elif mid * mid < n:
            l = mid + 1
        else:
            r = mid - 1
    return 0

if __name__ == '__main__':
    print(solution1(9), solution2(9))
    print(solution1(693953651), solution2(693953651))
    print(solution1(756580036), solution2(756580036))
