class User:
    def __init__(self,login_attempts):
        self.login_attempts=login_attempts
    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f"现在的次数为：{self.login_attempts}")
    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"现在的次数又重新变为：{self.login_attempts}")
user1=User(5)
user1.increment_login_attempts()
user1.reset_login_attempts()