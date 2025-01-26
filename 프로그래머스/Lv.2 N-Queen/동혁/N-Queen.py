def check(ls, new):
    row = len(ls)
    for i in range(row):
#         추가하려는 행에 특정 숫자가 존재한 경우 실패
#         대각선이면 실패
        if new == ls[i] or row - i == abs(ls[i] - new):
            return False
    return True

def dfs(n, ls):
#     모두 배치한 경우
#     한 행에 한개의 퀸만 배치 가능(가로,세로,대각을 이동할 수 있어서)
    if len(ls) == n:
        return 1

    cnt = 0
    for i in range(n):
        if check(ls, i):
            ls.append(i)
            cnt += dfs(n, ls)
            ls.pop()
    return cnt

def solution(n):
    return dfs(n, [])
