from collections import deque


def solution(queue1, queue2):
    answer = 0

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    limit = (len(queue1)) * 4

    #     연산용
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    total = tot1 + tot2

    #     전체합이 홀수면 같을 수 없다.
    if total % 2 != 0:
        return -1

    while True:
        #         높은 큐에서 낮은 큐로 이동
        if tot1 > tot2:
            target = queue1.popleft()
            queue2.append(target)
            tot1 -= target
            tot2 += target
            answer += 1

        elif tot1 < tot2:
            target = queue2.popleft()
            queue1.append(target)
            tot1 += target
            tot2 -= target
            answer += 1
        #             같다면 탈출
        else:
            break
        #             끝까지 탈출하지 못했을 때
        if answer == limit:
            answer = -1
            break
    return answer