from collections import deque


def solution(number, k):
    # 시간 단축을 위해 덱 사용
    answer = deque([])
    index = deque([])
    value = deque([])
    # sum()을 사용하니까 타임 오버
    num = 0

    for n, i in enumerate(number + [0]):
        # answer가 들어있고, num이 넘는다면
        while value and num > k:
            num -= value.popleft()
            index.popleft()

        if num == k:
            answer.append([index[0], index[-1]])

        num += i
        value.append(i)
        index.append(n)

    return sorted(answer, key=lambda x: x[1] - x[0])