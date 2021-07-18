class sign_up:
    def __init__(self,userID,user,password):
        self.user = user
        self.password = password
        self.userID = userID
    def sign_up(self):
        try:
            A = str(self.userID)
            f = open(f'user\\{self.userID}','x')
            f.write(f"{A}\n{self.user}\n{self.password}")
        except FileExistsError:
            return 401
