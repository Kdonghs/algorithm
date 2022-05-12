def solution(w,h):
    from math import gcd
    answer = w*h
    g = gcd(w,h)
    return answer - (w+h-g)