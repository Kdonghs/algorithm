from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for k in course:
        candidates = []
        for menu_li in orders:
            # 코스의 길이만큼 메뉴의 조합
            for li in combinations(menu_li, k):
                # 글자를 정렬
                # 'ab' == 'ba'
                res = ''.join(sorted(li))
                candidates.append(res)

        # 중복된 갯수 세주고 정렬
        sorted_candidates = Counter(candidates).most_common()
        # 1번 초과 메뉴가 나왔고, 나온 빈도가 가장 많은 메뉴 추가
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)