n=int(input('num of contact u want to add: '))
a={}
for i in range (0,n):
    xi=str(input("enter name: "))
    yi=int(input("enter phone num: "))
    zi=str(yi)
    if len(zi)!=10:
        print('unvalied mobile num')
        continue
    else:
        a[xi]=yi
c=input('if u want to see contact press enter')
print(a)
           
