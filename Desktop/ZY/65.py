class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"这家餐馆叫做：{self.restaurant_name},菜系类型为：{self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业！")
restaurant=Restaurant("湘味斋","川菜")
restaurant.describe_restaurant()
restaurant.open_restaurant()
        