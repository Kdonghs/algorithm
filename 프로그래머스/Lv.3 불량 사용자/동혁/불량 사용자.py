from itertools import permutations
import re


def solution(user_id, banned_id):
    #     re에서는 .이 이스케이프 문자
    #     *은 앞 문자를 반복
    ban = [i.replace("*", ".") for i in banned_id]

    result = list()

    #     순열의 경우의 수
    for i in permutations(user_id, len(ban)):
        i = list(i)
        check = True

        for j in range(len(i)):
            #             조건에 부합한 경우
            #             문자가 동일하면서, 길이도 같음
            if (re.match(ban[j], i[j]) and (len(i[j]) == len(ban[j]))):
                continue
            else:
                check = False
                break
        if (check):
            if (sorted(i) not in result):
                result.append(sorted(i))

    return len(result)