import math


def solution(n, stations, w):
    answer = 0
    start = 1
    # 커버리지
    std = w * 2 + 1

    # 기지국간의 커버하지 않는 거리를 구해서 힐요한 기지국의 수를 구해서 나눔(올림)
    for i in stations:
        gab = i - start - w
        if gab > 0:
            answer += math.ceil(gab / std)
        start = i + w + 1

    # 마지막 기지국으로부터 끝까지 영역을 계산
    gab = n - stations[-1] - w
    if gab > 0:
        answer += math.ceil(gab / std)

    return answer
