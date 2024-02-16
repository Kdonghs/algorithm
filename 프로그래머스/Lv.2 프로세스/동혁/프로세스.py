def solution(priorities, location):
    answer = 0
    # 프로세스와 가중치 묶기
    queue = [[n, i] for n, i in enumerate(priorities)]

    while True:
        # 맨 앞 프로세스를 꺼내서 뒤의 가중치 비교
        # 가중치가 밀리면 마지막에 추가
        x = queue.pop(0)
        if any(x[1] < i[1] for i in queue):
            queue.append(x)
        else:
            answer += 1
            # 현재 종료된 프로세스가 대상 프로세스면 반복 종료
            if x[0] == location:
                break

    return answer