def user():
    print"We come to our System"
    print"What do you want to do?"
    print " "
    print "1) Registration"
    print "2) Login"
    print "3) Post content"
    print "4) comment"
    print "5) logout"
    print " "

def register(full_name,username,email,password,confirm_password):
    print "full in the field to register"

def login(email,password):
    print"Login with your correct  username and password"

def post(title,content):
    print "post your content here!"

def comment(comment):
    print("post your comments here!")

loop = 1
choice = 0
while loop == 1:
    choice == user()
    if choice == 1:
        register(input("full_name"),input("username"),input("email"),input("passwors"),input("confrim_password"))
    elif choice == 2:
        login(input("email"),input("password"))
    elif choice == 3:
        post(input("title"), input("content"))
    elif choice == 4:
        comment(input(comment))

    elif choice == 5:
        loop == 0
    print "Thanks you for using our System"
    