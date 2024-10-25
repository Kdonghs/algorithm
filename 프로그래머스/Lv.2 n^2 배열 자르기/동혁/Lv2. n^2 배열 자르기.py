def solution(n, left, right):
    li = []
    # 모든 리스트
    # for i in range(n):
    #     for j in range(i):
    #         li.append(i+1)
    #     for j in range(i,n):
    #         li.append(j+1)
    # print(li)

    # 범위만큼 리스트 생성
    a = left // n
    b = left % n

    c = right // n
    d = right % n

    for i in range(a, c + 1):
        for j in range(i):
            li.append(i + 1)
        for j in range(i, n):
            li.append(j + 1)
    return li[b:(c - a) * n + d + 1]
