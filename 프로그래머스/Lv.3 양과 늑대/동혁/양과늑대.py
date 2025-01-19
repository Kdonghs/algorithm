def solution(info, edges):
    answer = []
    visited = [0] * len(info)

    def dfs(sheep, wolf):
        #         늑대보다 양이 많았을때 결과 추가
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for p, c in edges:
            #             부모노드는 방문 했지만, 자식 노드는 방문하지 않은 경우
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[c] = 0

    visited[0] = 1
    dfs(1, 0)

    return max(answer)

