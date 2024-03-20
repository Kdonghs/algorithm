# 점화식
# 1->1
# 2->2
# 3->3
# 4->5
# 5->8...
def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    li = [0] * n
    li[0] = 1
    li[1] = 2
    for i in range(2, n):
        li[i] = (li[i - 1] + li[i - 2]) % 1000000007
    return li[n - 1]