a=[9,5,2,4,7,8,6,1,3]
for i in range (0,len(a)):
    j=i+1
    while j<len(a) and a[i]>a[j]:
        a[i],a[j]=a[j],a[i]
        j+=1
print(a)
