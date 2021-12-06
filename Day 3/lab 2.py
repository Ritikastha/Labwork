a=int(input("enter marks of 1st subject"))
b=int(input("enter marks of 2nd subject"))
c=int(input("enter marks of 3rd subject"))
d=int(input("enter marks of 4th subject"))
per=(a+b+c+d)/400*100
if per>70:
 print("Distinction")
elif per> 60:
  print("first")
elif per>40:
    print("pass")
elif per<40:
    print("fail")