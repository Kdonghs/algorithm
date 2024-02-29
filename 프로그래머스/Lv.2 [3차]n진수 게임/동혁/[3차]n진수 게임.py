# n진수 변환
def convert(number, n):
    if number == 0:
        return '0'
    NUMBERS = "0123456789ABCDEF"
    res = ""
    while number > 0:
        number, mod = divmod(number, n)
        res += NUMBERS[mod]
    return res[::-1]


def solution(n, t, m, p):
    answer = ''
    words = ''
    p = p - 1

    for num in range(t * m):
        words += convert(num, n)

    while 1:
        if len(answer) == t:
            break

        answer += words[p]
        p += m
    return answer