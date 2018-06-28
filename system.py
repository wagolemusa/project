class User():

    #enables users to create accounts
    def register(self):
        print"*****************************"
        print"Welcome To Our System"
        print " "
        full_name = raw_input("Enter Your Names")
        username  = raw_input("Enter Your Username")
        email     = raw_input("Enter Your Email")
        password  = raw_input("Enter Your password")
        confirm_password = raw_input("Confirm Your passward")

        print"You are successfully Signup"
        print " " 

        print"Would do you like to sigin?"
        print " "
        print"*********************************"
        
        #enable users to Signin
    def login(self):
        username = raw_input("Enter Your Username")
        password = raw_input("Enter Your Password")
        print " "
        print"Welcome %s You successfully logged in" %username
        print " "
        print"***********************************"
        print"You go a head and post Your content"
        #enable user to post content
    def post(self):
        title = raw_input("Enter Title")
        content = raw_input("Enter Content Here")
        print" "

        print"Would do like to comment on your post"
        print"**************************************"
        
        #enables other people to post there reviews
    def post_comment(self):
        comment = raw_input("Post Your reviews here!")
        print"***************************************"

system = User()
system.register()
system.login()
system.post()
system.post_comment()


    


