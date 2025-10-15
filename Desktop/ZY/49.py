while True:
    age=input("输入你的年龄：")
    age=int(age)
    if age<3:
        print("免门票")
    elif 3<=age<12:
        print("10$")
    else:
        print("12$")
