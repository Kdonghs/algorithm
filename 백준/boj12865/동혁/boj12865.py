n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        a = thing[i][0]
        b = thing[i][1]

        if j<a:
            d[i][j] = d[i-1][j] #가중치보다 작으면 이전값 대입
        else:
            #n + w-n , d[i-1][j]중 큰값
            d[i][j] = max(d[i-1][j], d[i-1][j-a]+b)

print(d[n][k])