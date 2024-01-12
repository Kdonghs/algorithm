import heapq
import sys

N = int(input())
nums = [int(input()) for _ in range(N)]
left, right = [], []

for i in nums:

    if len(left) == len(right):
        #좌우의 크기가 같다면 왼쪽에 대입
        heapq.heappush(left,(-i,i))
    else:
        heapq.heappush(right,(i,i))

    if right and left[0][1] > right[0][1]:
        a, b = heapq.heappop(left)[1], heapq.heappop(right)[1]
        heapq.heappush(left, (-b, b))
        heapq.heappush(right, (a, a))
    print(left,right)
    print(left[0][1])