class Restaurant:   #定义类
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type         #初始化属性
    def describe_restaurant(self):
        print(f"这家餐馆叫做：{self.restaurant_name},菜系类型为：{self.cuisine_type}")
        #定义两个方法
restaurant=Restaurant("湘味斋","川菜")
restaurant.describe_restaurant()  
restaurant=Restaurant("粤味源","粤菜")
restaurant.describe_restaurant()  
restaurant=Restaurant("山西面馆","晋菜")
restaurant.describe_restaurant()                    #调用方法
