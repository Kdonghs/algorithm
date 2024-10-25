def solution(routes):
    # 입구의 위치로 정렬
    routes.sort()
    # 최소 1대의 카메라 존재
    answer = 1
    start = routes[0][0]
    end = routes[0][1]

    # 시작과 끝 사이에 다른 차량의 시작이 없다면 겹치는게 없다.
    # 겹치면 중복되는 부분을 시작과 끝으로 해 교집합을 구한다.
    # 겹치는게 없다면 새로운 위치에 카메라를 설치한다.
    for a, b in routes[1:]:
        if start <= a <= end:
            start = a
            end = min(end, b)
        else:
            start = a
            end = b
            answer += 1
    return answer