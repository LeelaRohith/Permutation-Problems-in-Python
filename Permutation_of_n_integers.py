num=[int(x) for x in input('Enter the numbers : ').split()]
permutation=[[]]
for i in num:
    curr=[]
    for l in permutation:
        for j in range(0,len(l)+1):
            l.insert(j,i)
            temp=list(l)
            curr.append(temp)
            l.remove(i)
    permutation=curr
print('Possible Permutations : ',permutation)