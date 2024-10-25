def find(tree, money, number, answer):
    # 루트까지 왔거나 돈이 1원 미만일때
    if tree[number] == number or (money // 10 == 0):
        answer[number] += money
        return

    # 위로 올릴 돈
    send = money // 10
    # 내 돈
    mine = money - send
    answer[number] += mine

    # 트리,보내는돈,부모노드,잔고
    find(tree, send, tree[number], answer)
    return


def solution(enroll, referral, seller, amount):
    n = len(enroll)  # 총 사람 수(민호 포함 X)
    answer = [0] * (n + 1)  # 민호 포함
    tree = [i for i in range(n + 1)]
    d = {}

    # 딕셔너리 생성
    for i in range(n):
        d[enroll[i]] = i + 1

    # 부모 맵핑
    for i in range(n):
        if referral[i] == "-":  # 민호가 추천인
            tree[i + 1] = 0
        else:
            tree[i + 1] = d[referral[i]]

    for i in range(len(seller)):
        find(tree, amount[i] * 100, d[seller[i]], answer)
    return answer[1:]