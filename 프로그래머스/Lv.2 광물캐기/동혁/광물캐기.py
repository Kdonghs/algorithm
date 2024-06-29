def solution(picks, minerals):
    answer = 0
    mine = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]
    price = []

    for n, i in enumerate(mine):
        I = 0
        S = 0
        for j in i:
            if j == 'diamond':
                I += 5
                S += 25
            elif j == 'iron':
                I += 1
                S += 5
            elif j == 'stone':
                I += 1
                S += 1
        price.append([len(i), I, S])

    if len(price) > sum(picks):
        price = price[:sum(picks)]
    price.sort(key=lambda x: [x[2], x[1], x[0]], reverse=True)

    for i in price[:picks[0]]:
        answer += i[0]
    for i in price[picks[0]: picks[0] + picks[1]]:
        answer += i[1]
    for i in price[picks[0] + picks[1]: picks[0] + picks[1] + picks[2]]:
        answer += i[2]

    return answer