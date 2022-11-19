from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    piece = set()

    for i in topping:
        dic[i] -= 1
        piece.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(piece):
            answer += 1
    return answer