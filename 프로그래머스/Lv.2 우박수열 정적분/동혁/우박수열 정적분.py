# 평행 사변형 넓이를 반환
# 높이는 항상 1이여서 배재
def cal(a, b):
    return (abs(a) + abs(b)) / 2


def solution(k, ranges):
    space = []
    answer = []

    #     점 위치 구하기
    while k > 1:
        temp = k
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        space.append(cal(temp, k))
    # print(space)

    N = len(space)
    for a, b in ranges:
        if N + b >= a:
            answer.append(sum(space[a:N + b]))
        else:
            answer.append(-1)

    return answer