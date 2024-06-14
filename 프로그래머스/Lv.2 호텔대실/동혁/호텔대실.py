def solution(book_time):
    answer = 1

    li = [[int(i[0][:2]) * 60 + int(i[0][3:]), int(i[1][:2]) * 60 + int(i[1][3:]) + 10] for i in book_time]
    li.sort()

    heap = [0 for i in range(60 * 24 + 10)]
    for i in li:
        for j in range(i[0], i[1]):
            heap[j] += 1

    return max(heap)