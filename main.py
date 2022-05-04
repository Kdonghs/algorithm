import sys
import heapq

n=int(sys.stdin.readline().strip())
li=[]

for i in range(n):
    a=int(sys.stdin.readline().strip())

    if a==0:
        if len(li)==0:
            print(0)
            continue
        b=heapq.heappop(li)
        print(-b)
        continue
    heapq.heappush(li,-a)