def build_profile(first,last,**user_info):
    user_info["first_name"]=first
    user_info["last_name"]=last
    return user_info
user=build_profile("Shuo","Wang",loction="China",age=22)
print(user)
