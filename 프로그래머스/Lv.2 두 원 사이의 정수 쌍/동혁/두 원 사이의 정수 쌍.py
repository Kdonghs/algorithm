import math

def solution(r1, r2):
    answer = 0
    # 한 개의 사변만 구해서 더함
    for x in range(1, r2 + 1):
        # 한 열에서 구할 수 있는 점의 수
        # a^2 + b^2 = c^2
        # 내부 원은 내림, 외부 원은 올림으로 계산(내부 원과 외부 원이 겹치면 갯수에 포함함)
        outer = math.floor(math.sqrt(r2 ** 2 - x ** 2))
        if r1>x:
            inner = math.ceil(math.sqrt(r1 ** 2 - x ** 2))
        else:
            inner=0

        answer += (outer - inner + 1)
    return answer * 4

print(solution(2,3))