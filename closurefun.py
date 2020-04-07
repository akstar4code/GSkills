def logger(msg):
    def login(id):
        print('Login Details:\nuser and id : ',msg,id)
    return login
user = input()
userlog = logger(user)
userlog(2563)