a=input('enter list of  num : ')
b=input('enter a num you want to search : ')
for i in range (0, len(a)):
    
    if a[i]==b:
        print('the num you search is present at ', i+1, ' th position in the list')
        break

else:
    print('num you want to search for is not present in the list')
        

