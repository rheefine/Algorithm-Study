# 44ms

import sys

dq = [0] * 10001 * 2
head = 10000
tail = 10000

def push_r(num):
    global head 
    head -= 1
    dq[head] = num

def push_l(num):
    global tail
    dq[tail] = num
    tail += 1

def size():
    return tail - head

def empty():
    if size() == 0:
        return 1
    else:
        return 0

def pop_r():
    global head
    if empty() == 0:
        result = dq[head]
        head += 1
        return result
    else:
        return -1

def pop_l():
    global tail
    if empty() == 0:
        tail -= 1
        return dq[tail]
    else:
        return -1

n = int(sys.stdin.readline())

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front":
        push_r(int(cmd[1]))
    elif cmd[0] == "push_back":
        push_l(int(cmd[1]))
    elif cmd[0] == "pop_front":
        print(pop_r())
    elif cmd[0] == "pop_back":
        print(pop_l())
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
    elif cmd[0] == "front":
        if empty() == 0:
            print(dq[head])
        else:
            print(-1)
    elif cmd[0] == "back":
        if empty() == 0:
            print(dq[tail - 1])
        else:
            print(-1)
