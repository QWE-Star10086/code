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
user1=User("bo","he","dongbei","27")
user1.describe_user()
user1.greet_user()
user2=User("zhao","yuqi","hebei",24)
user2.describe_user()
user2.greet_user()
user3=User("wei","guoqiang","shandong",23)
user3.describe_user()
user3.greet_user()



        