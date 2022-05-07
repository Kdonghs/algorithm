from collections import defaultdict

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k=2
li = defaultdict(list)
stop = []
result = [0 for i in range(len(id_list))]

for i in report:
    a,b = i.split()
    if a in li[b]:
        continue
    li[b].append(a)
print(li)

for i in li:
    if len(li[i])>=k:
        stop.append(i)

print(stop)

for i in li:
    if i in stop:
        for j in li[i]:
            print(id_list.index(j))
            result[id_list.index(j)]+=1
print(result)

def a():
    li = defaultdict(list)
    stop = []
    result = [0 for i in range(len(id_list))]

    for i in report:
        a, b = i.split()
        if a in li[b]:
            continue
        li[b].append(a)

    for i in li:
        if len(li[i]) >= k:
            stop.append(i)


    for i in li:
        if i in stop:
            for j in li[i]:
                print(id_list.index(j))
                result[id_list.index(j)] += 1
    print(result)