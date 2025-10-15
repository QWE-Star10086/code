sandwich_orders=["a","b","c"]
finished_orders=[]
while sandwich_orders:     #循环
    current_orders=sandwich_orders.pop()   #随机弹出
    print(f"l made you {current_orders}.")  #挨个打印
    finished_orders.append(current_orders)   #加入
print(finished_orders)                        #统一打印
