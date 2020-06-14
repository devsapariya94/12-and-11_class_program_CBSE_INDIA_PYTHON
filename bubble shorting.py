a=[1,9,7,5,6,3,4,8]
n=0
for i in range (0,len(a)):
    for j in range (1,len(a)):
        if a[j]<a[j-1]:
            a[j-1],a[j]=a[j],a[j-1]
            n+=1
print(a)
print('number of interchange=',n)
