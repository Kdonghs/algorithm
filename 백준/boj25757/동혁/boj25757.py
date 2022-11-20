n,w=input().split()
li=[]
for i in range(int(n)):
    li.append(input())
if w=='Y':
    print(len(list(set(li))))
elif w=='F':
    print(len(list(set(li)))//2)
elif w=='O':
    print(len(list(set(li)))//3)