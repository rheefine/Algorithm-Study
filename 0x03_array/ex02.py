def solution1(arr, n):
    cnt = [0] * 101
    for i in arr:
        if cnt[100 - i] == 1:
            return 1
        cnt[i] = 1
    return 0            

if __name__ == '__main__':
    arr = [1,52,48]
    print(solution1(arr, 3))
    arr2 = [50,42]
    print(solution1(arr2, 2))
    arr3 = [4,13,63,87]
    print(solution1(arr3, 4))
