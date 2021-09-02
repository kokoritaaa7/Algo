import sys

for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip()
    length = int(sys.stdin.readline())
    if length:
        li = list(sys.stdin.readline()[1:-2].split(','))
    else:
        _ = sys.stdin.readline()
        li = []

    dCnt = cmd.count('D')
    if dCnt > length:
        print('error')
        continue
    elif dCnt == length:
        print('[]')
        continue
    else:
        Dlist = list(map(len, cmd.split('R')))
        popLeft = sum(Dlist[0::2])
        popRight = sum(Dlist[1::2])

        if popRight:
            li = li[popLeft:-popRight]
        else:
            li = li[popLeft:]

        if len(Dlist) % 2 == 0:
            li.reverse()
        print('[' + ','.join(li) + ']')