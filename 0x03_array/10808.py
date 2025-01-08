s = input()

cnt = [0] * 26

for e in s:
    cnt[ord(e) - ord('a')] += 1

for n in cnt:
    print(n, end=' ')
