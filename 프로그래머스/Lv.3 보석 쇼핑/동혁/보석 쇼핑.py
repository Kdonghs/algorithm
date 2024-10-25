from collections import defaultdict


def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))
    start = 0
    end = 0
    dic = defaultdict(int)

    dic[gems[end]] += 1

    while start < len(gems) and end < len(gems):
        if len(dic) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            else:
                dic[gems[start]] -= 1
                if dic[gems[start]] == 0:
                    del dic[gems[start]]
                start += 1
        else:
            end += 1
            if end == len(gems):
                break
            dic[gems[end]] += 1

    return [answer[0] + 1, answer[1] + 1]
