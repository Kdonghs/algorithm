def solution(phone_book):
    answer = True
    hash_map = {}

    # hash map생성
    for i in phone_book:
        hash_map[i] = 1

    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            # 각 번호마다 있는지 검사
            # 각 번호의 합이 원래 번호 와 같으면 안됨(자기자신을 참조하게 됨)
            #  dic는 해쉬 테이블을 사용해서 검색속도가 O(1)
            if temp in hash_map and temp != i:
                answer = False

    return answer
