people={
    "people_1":{
        "first_name":"Kobe",
        "last_name":"Bryant",
        "age":41,
        "city":"los_angles",
        },
    "people_2":{
        "first_name":"len",
        "last_name":"jjk",
        "age":25,
        "city":"ch"
        },
    "people_3":{
        "first_name":"hhj",
        "last_name":"jack",
        "age":29,
        "city":"xz",
        }                             #嵌套字典
  }
for name,name_info in people.items():  #遍历字典
    print(f"\nusername:{name}")
    full_name=f"{name_info["first_name"]}{name_info["last_name"]}"
    ages=name_info["age"]
    loction=name_info["city"]           #将关联值赋予变量
    print(f"\nFull name:{full_name}")
    print(f"\nAge:{ages}")
    print(f"\nwhere:{loction}")           #分别打印