# 피사노 주기
#피보나치 수열은 일정 주기마다 값이 반복된다.
#주기는 m=10^k, m//10 * 15
N = int(input())

mod = 1000000
fibo = [0, 1]
p = mod // 10 *15

for i in range(2,p):
    fibo.append(fibo[i-1]+fibo[i-2])
    fibo[i] %= mod

print(fibo[N%p])