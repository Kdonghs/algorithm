import heapq


def solution(jobs):
    answer = 0
    now = 0  # 현재시간
    i = 0  # 처리개수
    start = -1  # 마지막 완료시간
    heap = []

    while i < len(jobs):
        for job in jobs:
            # 현재 시간내 처리 가능한 job
            if start < job[0] <= now:
                # heappop은 가장 작은 원소를 가져옴
                heapq.heappush(heap, [job[1], job[0]])
        print(heap)
        if heap:
            # 가장 작은 job을 가져옴
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1]
            i += 1
        else:
            # job이 없다면 시간만 증가
            now += 1

    # 평균시간 반환
    return answer // len(jobs)
