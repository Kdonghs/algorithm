# a^2+b^2=c^2
# 찍을 수 있는 점의 범위
def solution(k, d):
    answer = 0

    for i in range(0, d + 1, k):
        limit = int((d * d - i * i) ** 0.5)
        answer += (limit // k) + 1

    return answer