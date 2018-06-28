class User():

    def register(self):
        print"*********************************"
        print "Welcome To our System"
        print " "
        full_name = raw_input("Enter Your Full name:")
        username = raw_input("Enter Your Username:")
        email = raw_input("Enter Your Email")
        password = raw_input("Enter Your password:")
        confirm_password = raw_input("Confirm your password:")
        all_names = username

        print "You are successfullfy Siginup"
        print " "
        
        print"Would do you Like to Sigin Now?"
        print " "
        print"*********************************"
    def login(self):
        username = raw_input("Enter Your Username:")
        password = raw_input("Enter Your Password:")
        print " "
        print "Welcame %s you are successfullfy logged in " %username
        print " "
        print" You can go a head and post"
        print"*********************************"
    def post(self):
        title = raw_input("Enter Title")
        content = raw_input("Enter Content")

        print " "
        print"Would you like to comment to your post?"
        print"*********************************"
    def post_comment(self):
        comment = raw_input("Enter comment")
        print " "

coolins = User()
coolins.register()
coolins.login()
coolins.post()
coolins.post_comment()