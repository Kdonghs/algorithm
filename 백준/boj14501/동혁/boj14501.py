n = int(input())
t = []
p =[]
for i in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)

dp = [0]*100
for i in range(n):
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    if dp[i + t[i]] < dp[i] + p[i]:
        dp[i +t[i]] = dp[i] + p[i]
print(dp[n])