def solution(s):
    answer = 0

    # 모든 문자열 순회
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            temp = s[i:j]
            # 뒤집은 문자열이 현재 문자열과 같다면 수행
            if temp == temp[::-1]:
                # 길이가 더 긴 문자열로 대치
                answer = max(answer, len(temp))

    return answer
