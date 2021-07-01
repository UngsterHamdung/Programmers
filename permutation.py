mylist = [1,2,3,4]
def solution(mylist):
mylist.sort()
for i in range(len(mylist)):
mylist[i] = str(mylist[i])
result = list(map(''.join, itertools.permutations(mylist)))
for i in range(len(result)):
result[i] = list(map(int,result[i]))
return result
print(solution(mylist))
