def changMin(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def solution(plans):
    #     시간을 분으로 변경 및 정렬
    for plan in plans:
        plan[1] = changMin(plan[1])
        plan[2] = int(plan[2])
    plans.sort(key=lambda x: x[1])

    answer = []
    stack = []
    current_time = 0

    while plans:
        name, start_time, duration = plans.pop(0)

        # 새 과목 시작전 시간이 있는 경우
        if current_time < start_time:
            # 이전 과제를 처리할 수 있는 시간 계산
            while stack and current_time < start_time:
                prev_name, remaining_time = stack.pop()
                if current_time + remaining_time <= start_time:
                    # 이전 과제 완료
                    current_time += remaining_time
                    answer.append(prev_name)
                else:
                    # 이전 과제를 다 처리 못하고 남으면 다시 스택에 저장
                    stack.append((prev_name, remaining_time - (start_time - current_time)))
                    current_time = start_time
                    break

        # 새로운 과제 시작
        current_time = start_time
        stack.append((name, duration))

    while stack:
        name, remaining_time = stack.pop()
        answer.append(name)

    return answer
