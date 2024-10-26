from datetime import datetime
from dateutil.relativedelta import relativedelta


def solution(today, terms, privacies):
    answer = []
    dic = {}
    now = datetime.strptime(today, '%Y.%m.%d')

    for i in terms:
        a, b = i.split()
        dic[a] = int(b)

    for n, i in enumerate(privacies):
        a, b = i.split()
        lim = datetime.strptime(a, '%Y.%m.%d')
        if (lim + relativedelta(months=dic[b]) - relativedelta(days=1)) < now:
            answer.append(n + 1)

    return answer