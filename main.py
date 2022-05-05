import sys

n,m = map(int,sys.stdin.readline().strip().split())
know = set(sys.stdin.readline().strip().rsplit()[1:])
li=[]

if len(know)==0:
    print(m)
else:
    for i in range(m):
        party = set(sys.stdin.readline().strip().split()[1:])
        li.append(party)

    for _ in range(m):
        for i in li:
            if know & i:
                know = know.union(i)

    count=0
    for i in li:
        if not know & i:
            count+=1

    print(count)