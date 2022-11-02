n=int(input())
li = list(map(int,input().split()))
sum=0
for i in li:
    sum=100-(100-sum)/100*(100-i)
    print(sum)