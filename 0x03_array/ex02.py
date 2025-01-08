# 시간 복잡도: O(n)
def solution1(arr, n):
    num = [0] * 101
    for i in range(n):
        num[arr[i]] = 1 
    for i in range(101):
        if num[i] == 1 and num[100-i] == 1 and i != 100-i:
            return 1
    return 0

if __name__ == '__main__':
    arr = [1,52,48]
    print(solution1(arr, 3))
    arr2 = [50,42]
    print(solution1(arr2, 2))
    arr3 = [4,13,63,87]
    print(solution1(arr3, 4))
