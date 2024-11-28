import heapq


def solution(n, k, enemy):
    answer = 0
    heap = []
    count = 0

    for i in enemy:
        #         절대값 기준으로 내림차순으로 정렬
        heapq.heappush(heap, -i)
        count += i
        if count > n:
            if not k:
                return answer
            #             무적권이 있다면 가장 큰 값을 뺴고 무적권 감소
            count += heapq.heappop(heap)
            k -= 1
        answer += 1
    return answer