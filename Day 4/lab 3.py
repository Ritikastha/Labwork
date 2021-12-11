# Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".

a=int(input("enter your age"))
b=input("enter your gender")
if b=="female" :{
print("she will work in urben area")
} 
elif b=="male" and a>20 or a<40:{
   print("he may work anywhere")
}  
elif b=="male" and a>40 or a<60 :{
  print("he will work in urban area")
}

       



