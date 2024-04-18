from collections import defaultdict
def solution(weights):
    answer = 0
    dic = defaultdict(int)

    for i in weights:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in dic:
        # 항목이 중복된다면
        if dic[i] > 1:
            answer += (dic[i] * (dic[i] - 1)) / 2
        if i * 2 in dic:
            answer += dic[i] * dic[2 * i]
        if i * 2 / 3 in dic:
            answer += dic[i] * dic[i * 2 / 3]
        if i * 3 / 4 in dic:
            answer += dic[i] * dic[i * 3 / 4]
    return answer
