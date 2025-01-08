# 시간 복잡도: O(logN)
def soluition1(n):
    i = 1
    while(2 * i <= n):
        i *= 2
    return i

if __name__ == "__main__":
    print(soluition1(5))
    print(soluition1(97615282))
    print(soluition1(1024))
    print(soluition1(1))
