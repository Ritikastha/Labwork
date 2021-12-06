#Take username and password from user and check it again for the three times whether the user has entered the right username and password.
#  If yes then print a message "Logged in Successfully", 
# if not then print invalid credentials for consecutive 3 times and if the limit exceeds than print "Attempt finished".

for i in range(0,3):
    username="Ram"
    Password="abc"
    print("enter your credentials")
    a=input("enter username")
    b=input("enter password")
    if a==username and b==Password:
        print("logged in succesfully")
    else:
       print("invalid credentials")
    print("attempt finished")
 

