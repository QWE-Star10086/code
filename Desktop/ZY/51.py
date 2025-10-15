sandwich_orders=["a","b","c","b","b"]
print("\nb卖完了")
while "b" in sandwich_orders:   #在菜单中循环b
    sandwich_orders.remove("b")   #删除b
finished_orders=[]
while sandwich_orders:     
    current_orders=sandwich_orders.pop()   
    print(f"l made you {current_orders}.")  
    finished_orders.append(current_orders)   
print(finished_orders)                      