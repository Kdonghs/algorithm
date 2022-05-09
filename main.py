numbers = [1,2,3,4,6,7,8,0]
li = [i for i in range(10)]

for i in numbers:
    li.remove(i)
print(sum(li))