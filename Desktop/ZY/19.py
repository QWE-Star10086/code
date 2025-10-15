name=["cat","tiger","lion","dog","fish"]
print(name[0:3])
print(name[1:4])
print(name[2:5])
friend=name[0:5]
name.append("monkey")
friend.append("snake")
print(name)
print(friend)
print(f"My favourite animals are:")
for a in name:
    print(a)
print(f"My friends's favourite animals are:")
for b in friend:
    print(b)