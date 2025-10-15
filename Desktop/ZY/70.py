class Restaurant:   #定义类
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type         #初始化属性
    def describe_restaurant(self):
        print(f"这家餐馆叫做：{self.restaurant_name},菜系类型为：{self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业！")    #定义两个方法
restaurant=Restaurant("湘味斋","川菜")              #创建实例
restaurant.describe_restaurant()                    #调用方法
restaurant.open_restaurant()
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=flavors
    def many_flavors(self):
        print(f"你想要的口味是：{self.flavors}")
my_flavors=IceCreamStand("睿星","甜品","香芋")
my_flavors.describe_restaurant()
my_flavors.many_flavors()
