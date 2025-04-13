import sys
from collections import deque

n = int(sys.stdin.readline().strip())

stack = deque()

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            pop_num = stack.pop()
            print(pop_num)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif cmd[0] == "push":
        stack.append(int(cmd[1]))
