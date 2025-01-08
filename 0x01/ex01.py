# 시간 복잡도: O(n)
def solution1(n):
    res = 0
    for i in range(1,n+1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res

# 시간 복잡도: O(1)
def solution2(n):
    res = 0
    max5 = n - (n % 5)
    max3 = n - (n % 3)
    max15 = n- (n % 15)
    res5 = (max5 + 5) * (max5 / 5) / 2 
    res3 = (max3 + 3) * (max3 / 3) / 2
    res15 = (max15 + 15) * (max15 / 15) / 2

    return res5 + res3 - res15

if __name__ == '__main__':
    for i in range(1, 16):
        print(solution1(i), solution2(i))
    print(solution1(16), solution2(16))
    print(solution1(34567), solution2(34567))
    print(solution1(27639), solution2(27639))
