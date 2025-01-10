dat = [-1]
pre = [-1]
nxt = [-1]
unused = 1

def insert(addr, num):
    global unused
    dat.append(-1)
    pre.append(-1)
    nxt.append(-1)
    dat[unused] = num
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    unused += 1

def traverse():
    cur = nxt[0]
    while(cur != -1):
        print(dat[cur], end = ' ')
        cur = nxt[cur]
    print()

def insert_test():
    print("****** insert_test *****\n")
    insert(0, 10)
    traverse()
    insert(0, 30)
    traverse()
    insert(2, 40)
    traverse()
    insert(1, 20)
    traverse()
    insert(4, 70)
    traverse()

if __name__ == "__main__":
    insert_test()
