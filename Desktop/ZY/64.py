def car_messages(maker,size,**kwargs):
    kwargs["maker"]=maker
    kwargs["size"]=size
    return kwargs
car=car_messages("subaru","outback",color="bule",tow_package=True)
print(car)