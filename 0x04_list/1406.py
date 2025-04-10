# 268ms

import sys
from collections import deque

text = sys.stdin.readline().strip()
m = int(sys.stdin.readline())

text_list = deque()
for i in range(len(text)):
   text_list.append(text[i])  

rotate_cnt = 0

for i in range(m):
   cmd = sys.stdin.readline().strip()
   if cmd == "L":
       if (len(text_list) > rotate_cnt):
           text_list.rotate(1)
           rotate_cnt += 1
   elif cmd == "D":
       if (rotate_cnt > 0):
           text_list.rotate(-1)
           rotate_cnt -= 1
   elif cmd == "B":
       if len(text_list) > rotate_cnt:
           text_list.pop()
   else:
       text_list.append(cmd[2])

text_list.rotate(-rotate_cnt)

print("".join(text_list))
