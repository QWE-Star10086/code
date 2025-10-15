visit_place={}
prompt="\nIf you could visit one place in the world,where would you go?"
prompt+="\n(Enter 'quit' when you are finished.)"
Poll_active=True
while Poll_active:
    name=input("\n请输入你的名字：")
    place=input("\n你最喜欢去的地方：")
    visit_place[name]=place
    repeat=input("\n还有人吗？(yes/no)")
    if repeat=="no":
        Poll_active=False
print("\n---poll result---")
for name,place in visit_place.items():
    print(f"{name} want to {place}.")
