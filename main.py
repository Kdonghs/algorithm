
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
li = {}
result =[]
answer = []
for i in record:
    io = i.split()
    if io[0]=='Enter':
        li[io[1]]=io[2]
    elif io[0]=='Change':
        li[io[1]] = io[2]
        continue
    result.append([io[1],io[0]])

for i in result:
    if i[1] =='Enter':
        answer.append(li[i[0]] + "님이 들어왔습니다.")
    else:
        answer.append(li[i[0]] + "님이 나갔습니다.")

def a():
    li = {}
    result = []
    answer = []
    for i in record:
        io = i.split()
        if io[0] == 'Enter':
            li[io[1]] = io[2]
        elif io[0] == 'Change':
            li[io[1]] = io[2]
            continue
        result.append([io[1], io[0]])

    for i in result:
        if i[1] == 'Enter':
            answer.append(li[i[0]] + "님이 들어왔습니다.")
        else:
            answer.append(li[i[0]] + "님이 나갔습니다.")