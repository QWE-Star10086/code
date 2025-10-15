class Restaurant:   #定义类
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0    #初始化属性
    def describe_restaurant(self):
        print(f"这家餐馆叫做：{self.restaurant_name},菜系类型为：{self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业！")
    def begin_number_served(self):
        print(f"就餐人数为：{self.number_served}")    #定义一个开始就餐的方法
    def update_number_served(self,number):           #定义更新人数的方法
        self.number_served=number                 #将初始人数赋值给更新后的属性number
    def increment_number_served(self,numbers):     #定义一个增加人数的方法
        self.number_served+=numbers                #现在人数为就餐人数加上增加人数
restaurant=Restaurant("湘味斋","川菜")              #创建实例
restaurant.describe_restaurant()                    #调用方法
restaurant.open_restaurant()
restaurant.update_number_served(50)
restaurant.begin_number_served()          #更新人数调用
restaurant.increment_number_served(6)
restaurant.begin_number_served()          #增加人数调用
