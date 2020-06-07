a=input('enter the binary num: ')
w=0
f=str(a)
for i in range (0,len(a)):
   x=(2**i)*int(a[i])
   w=w+x
print(w)
