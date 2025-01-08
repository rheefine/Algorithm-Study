def max_num(num, arr):
    tmp = arr[0]
    for i in range(1, num):
        if tmp <= arr[i]:
            tmp = arr[i]
    return tmp

if __name__ == '__main__':
    num = 4
    arr = [7, 10, 3, 8]
    print(max_num(num, arr))