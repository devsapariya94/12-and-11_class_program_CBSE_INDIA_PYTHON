thisdict =	{
  "dev1": "abc",
  "dev2": "xyz",
  "dev3": "pqr"
}
b=input('enter the username: ')
p=input('enter password: ')
z=thisdict.values()
a=str(b)
if a in  thisdict:
  
  if str(thisdict[a])==p:
      print('password is correct')
  else:
        print('password is incorrect')
else:
    print("username not found")

    
