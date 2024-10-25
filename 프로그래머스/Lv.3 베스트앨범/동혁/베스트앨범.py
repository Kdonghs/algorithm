from collections import defaultdict

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
def solution(genres, plays):
    answer = []
    dic=defaultdict(list)
    # 장르:[재생수, 고유번호]
    for i in range(len(genres)):
        dic[genres[i]] += [[plays[i],i]]

    # 재생수의 합이 큰 key로 정렬
    sorted_data = sorted(dic.items(), key=lambda x: sum(item[0] for item in x[1]), reverse=True)
    for i in sorted_data:
        for j in i[1:]:
            # 딕셔너리내 재생수가 큰 순서로 정렬해서 상위 2개만 answer에 저장
            for k in sorted(j, key=lambda x: x[0], reverse=True)[:2]:
                answer.append(k[1])

    return answer