# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
a=int(input("enter no of classes held"))
b=int(input("enter no of classes attended "))
per=(b/a)*100
print(f"Percentage of class attended is {per}")
if per>=75:
    print("student is allowed to sit in exam")
else:
    print("student is not allowed to sit in exam")
