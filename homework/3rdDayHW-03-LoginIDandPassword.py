username = input("Please enter your username : ")
password = input("Please enter your password : ")
print (username,"\nYou are now logged in successfully")

command = input("Please type a command :")
if command == "log off":
    print ("You have now been logged off again",username)
    username == ""
    password == ""

username = input("Please enter your username : ")
password = input("Please enter your password : ")
while (username !="username" and password !="password"):
    print ("Sorry username and password incorrect please re-enter for validation")
    username = input("Please enter your username : ")
    password = input("Please enter your password : ")
else:
    print (username,"You are now logged in successfully")