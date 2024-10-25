def solution(n, cores):
    #     코어의 수보다 job의 수가 적다면 리턴
    if len(cores) >= n:
        return n
    else:
        #         이진탐색
        #         처음 한바뀌는 모든 코어가 일을 수행할 수 있다.
        n -= len(cores)
        left = 1
        #         제일 느린 코어로 모든 일을 처리했을 경우
        right = max(cores) * n
        # print(left, right)

        while left < right:
            #             중간값(시간)
            mid = (left + right) // 2

            #             중간값으로 수행할 수 있는 일의 수를 구함
            jobs = 0
            for i in cores:
                jobs += mid // i

            if jobs >= n:
                right = mid
            else:
                left = mid + 1

        #         찾아낸 중간값으로 스케줄링 적용
        for i in cores:
            n -= (right - 1) // i

        #         스케줄링을 하고 남은 잉여값으로 해당하는 코어값을 찾음
        #         앞에서부터 딱 덜어지는 검사
        for m, i in enumerate(cores):
            if right % i == 0:
                n -= 1
                if n == 0:
                    #                     인덱스는 +1
                    return m + 1