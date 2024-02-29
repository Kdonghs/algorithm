import math

# 해당 진수로 바꾸기
def change(n, k):
    word = ""
    while n:
        word = str(n % k) + word
        n = n // k
    return word


def solution(n, k):
    # 0을 기준으로 나눔
    word = change(n, k).split('0')
    count = 0

    for w in word:
        # 0,1,빈공간은 continue
        if len(w) == 0:
            continue
        if int(w) < 2:
            continue

        # 소수인지 판단
        # 맨 처음 에라토스 테네스의 체로 구하니 시간 초과
        # 따라서 각각 판단
        prime = True
        for i in range(2, int(int(w) ** 0.5) + 1):
            if int(w) % i == 0:
                prime = False
                break
        if prime:
            count += 1

    return count