a=input('enter a string: ')
b=input('enter another string: ')
if len(a)!= len(b):
    print('the string are not equal')
else:
    for i in range (0, len(a)):
        if a[i]!=b[i]:
            print('the string are not equal')
            break
    else:
        print('they r same')
