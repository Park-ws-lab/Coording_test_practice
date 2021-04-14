array=[1,5,2,6,3,7,4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
answer = []
sort1=[]
for i in range(len(commands)):
    for j in range(commands[i][0]-1,commands[i][1]):
        sort1.append(array[j])
    sort1.sort()
    k=commands[i][2]
    answer.append(sort1[k-1])
    sort1=[]
print(answer)
