def solution(files):
    answer = []

    #     헤더,넘버,테일 구분
    for i in files:
        header = ''
        number = ''
        tail = ''

        for j in i:
            #             숫자이면서 테일이 비어있다면 넘버이다.
            if j.isdigit() and tail == '':
                number += j
            #             넘버가 나오기전 문자는 헤더이다.
            elif number == '':
                header += j
            #             헤더와 넘버가 존재하면 테일이다
            elif number != '':
                tail += j

        answer.append([header, number, tail])
    #     헤더는 대소문자구분 하지 않는다.
    #     넘버는 정수의 순서대로 정렬한다.
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(i) for i in answer]