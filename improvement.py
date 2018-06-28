class User():
    def __init__(self):
        self.databese={}
    #enables users to create accounts
    def register(self):
        print('*****************************')
        print('Welcome To Our System')
        print (' ')
        full_name = input('Enter Your Names ')
        username  = input('Enter Your Username ')
        email     = input('Enter Your Email  ')
        if email in self.databese:
            print('email is already taken')
        else:

            password  = input('Enter Your password ')
            confirm_password = input('Confirm Your passward ')
            self.reg(full_name,username,email,password,confirm_password)

    def reg(self,full_name,username,email,password,confirm_password):
        self.databese.update({username:password})
        print('Successfully Signup' + " " + username)

        print (' ')

        print('Would do you like to signin? ')
        print ('')
        print('*********************************')
        
        #enable users to Signin
    def login(self):
        username = input('Enter Your Username  ')
        password = input('Enter Your Password  ')
        self.log(username,password)

    def log(self,username, passward):
        if passward==self.databese[username]:
            print (' ')
            print('Welcome  You successfully logged in' + " " +username)
        else:
            print('Invalid Credentials')
            
        print (' ')
        print('***********************************')
        print('You go a head and post Your content ')

        #enable user to post content
    def post(self):
        title = input('Enter Title ')
        content = input('Enter Content Here ')
        print('')

        print('Would do like to comment on your post ')
        print('**************************************')
        
        #enables other people to post there reviews
    def post_comment(self):
        comment = input('Post Your reviews here! ')
        print('***************************************')

status = ''  
status = User()
status = input("Are you registered user? y/n? Press q to quit")
if status == "y":
    status.register()
elif status == "n":
    status.login()

#system = User()
#system.register()
#system.login()
#system.post()
#system.post_comment()