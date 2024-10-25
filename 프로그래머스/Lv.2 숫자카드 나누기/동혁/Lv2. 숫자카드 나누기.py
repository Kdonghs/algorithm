import math
def get_gcd(arr):
    g = arr[0]
    for i in range(1,len(arr)):
        g = math.gcd(g,arr[i])
    return g

def solution(arrayA, arrayB):
    res = 0
    A, B = get_gcd(arrayA), get_gcd(arrayB)

    for i in arrayB:
        if i % A == 0:
            break
    else:
        res = max(A, res)

        # 두 번째 조건
    for i in arrayA:
        if i % B == 0:
            break
    else:
        res = max(B, res)

    return res
