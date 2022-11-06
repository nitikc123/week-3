password=input("Enter a password:")
if((len(password)>=8) and (len(password)<=12)):
    password2=input("Confirm password")
    if password==password2:
        print("password set")
    else:
        print("sorry wrong password try again")
else:
    print("Sorry you entered less than 8 characters or more than 12 characters")



    


  
   