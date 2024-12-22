def solution(cards):
    answer = []
    check = [True] * len(cards)

    for n, isTure in enumerate(check):
        if isTure:
            temp = []
            target = n
            while True:
                if check[target]:
                    temp.append(cards[target])
                    check[target] = False
                    target = cards[target]-1
                else:
                    break
            answer.append(temp)

    answer.sort(key=lambda x: -len(x))
    if len(answer)==1:
        return 0
    return len(answer[0]) * len(answer[1])
