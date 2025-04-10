# 888ms

import sys

text = sys.stdin.readline().strip('\n')
m = int(sys.stdin.readline().strip('\n'))

data = [-1]
pre = [-1]
nxt = [1]

cursor = len(text)

for i in range(cursor):
    data.append(text[i])
    pre.append(i)
    nxt.append(i+2)

nxt[-1] = -1

for i in range(m):
    cmd = sys.stdin.readline().strip('\n')
    if cmd[0] == 'L':
        if pre[cursor] != -1:
            cursor = pre[cursor]
    elif cmd[0] == 'D':
        if nxt[cursor] != -1:
            cursor = nxt[cursor]
    elif cmd[0] == 'B':
        if pre[cursor] != -1:
            if nxt[cursor] != -1:
                pre[nxt[cursor]] = pre[cursor]
            nxt[pre[cursor]] = nxt[cursor]
            cursor = pre[cursor]
    elif cmd[0] == 'P':
        data.append(cmd[2])
        pre.append(cursor)
        nxt.append(nxt[cursor])
        if nxt[cursor] != -1:
            pre[nxt[cursor]] = len(data) - 1
        nxt[cursor] = len(data) - 1
        cursor = len(data) - 1
    
current = nxt[0]
while current != -1:
    print(data[current], end="")
    current = nxt[current]
