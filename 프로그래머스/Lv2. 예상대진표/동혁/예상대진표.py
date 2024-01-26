def solution(n, a, b):
    answer = 0
    # 숫자가 같을때까지 검사
    while a != b:
        answer += 1

        # 몇번쨰 매치인지 검사
        a = (a + 1) // 2
        b = (b + 1) // 2
    return answer