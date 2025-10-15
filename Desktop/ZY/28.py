current_users=["AAS","bbk","cdd","der","efg"]
new_users=["aas","ffd","jjk","hhl","cdd"]
current_users_lower=[user.lower() for user in current_users]
for user in new_users:
    if user.lower() not in current_users_lower:
        print(user)
    else:
        print("用户名已被占用，请重新输入")