active=True
while active:
    meua=input("配料表：")
    if meua=="quit":
        active=False
    else:   
        print(f"你需要增加{meua}配料")
