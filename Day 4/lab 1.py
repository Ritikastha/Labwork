#Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else
#print ‘COMMON YEAR’.
year=int(input("enter any year"))
if( year%4==0 and year%100!=0 or year%400==0):
    print("Leap year")
else:
        print("common year")