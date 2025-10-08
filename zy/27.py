users=["admin","jjk","li","bb","ajk"]
for user in users:
    if user=="admin":
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"Hello {user},thank you for logging in again.")
users=[]
if user in users:
     print(user)
else:
    print("We need you to find some users.")
    