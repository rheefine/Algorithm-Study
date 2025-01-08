# 시간 복잡도: O(n^2)
def solution1(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == 100:
                return 1
    return 0

# 시간 복잡도: O(n)
def solution2(arr, n):
    num = [0] * 101
    for i in range(n):
        num[arr[i]] = 1 
    for i in range(101):
        if num[i] == 1 and num[100-i] == 1 and i != 100-i:
            return 1
    return 0

if __name__ == '__main__':
    arr = [1,52,48]
    print(solution1(arr, 3), solution2(arr, 3))
    arr2 = [50,42]
    print(solution1(arr2, 2), solution2(arr2, 2))
    arr3 = [4,13,63,87]
    print(solution1(arr3, 4), solution2(arr3, 4))
