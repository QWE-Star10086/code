class User:
    def __init__(self,first_name,last_name,loction,age):
        self.first_name=first_name
        self.last_name=last_name
        self.loction=loction
        self.age=age
        print()
    def describe_user(self):
        print("---摘要---")
        print(f"\n姓名：{self.first_name}{self.last_name}\n住址：{self.loction}\n年龄：{self.age}")
    def greet_user(self):
        print(f"Hello {self.first_name}{self.last_name}")
class Privileges():
    def __init__(self, privileges="can oo"):
        self.privileges=privileges
    def show_privileges(self):
        print(f"管理员可以：{self.privileges}")
class Admin(User):
    def __init__(self, first_name, last_name, loction, age):
        super().__init__(first_name, last_name, loction, age)
        self.privileges=Privileges() 
action=Admin("Wang","Shuo","China","22")
action.describe_user()
action.privileges.show_privileges()




        
    