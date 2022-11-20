import math

room = int(input())
test = list(map(int,input().split()))
b,c = map(int, input().split())
viewer = room

for i in test:
    if i <= b:
        continue
    viewer += math.ceil((i-b)/c)
print(viewer)