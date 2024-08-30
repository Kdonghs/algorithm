def solution(tickets):
    answer = []
    # 현재 위치, 경로, tickets 인덱스
    q = [("ICN", ["ICN"], [])]

    while q:
        airport, path, used = q.pop(0)
        # 모든 티켓을 사용해야 함
        if len(used) == len(tickets):
            answer.append(path)

        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                q.append((ticket[1], path + [ticket[1]], used + [idx]))
#          알파벳 순서가 앞서는 경로를 반환
    answer.sort()
    return answer[0]
