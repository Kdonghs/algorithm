def solution(prices):
    length = len(prices)

    # answer을 max값으로 초기화
    answer = [i for i in range(length - 1, -1, -1)]

    # 주식 가격이 떨어질 경우 찾기
    # 주식 가격이 stack의 만 앞보다 값이 작으면 인덱스의 차이만큼이 된다.
    stack = []
    for i in range(length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer