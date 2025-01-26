# 3*2 = 3
# 3*3 = 0
# 3*4 = 11
# 3*6 = 41
# 3*8 = 153
# n * 4 - (n-2)
def solution(n):
    answer = [1, 1]

    for i in range(1, n + 1):
        if i % 2 == 0:
            answer.append((answer[-1] * 4 - answer[-2]) % 1000000007)
    return answer[-1]
