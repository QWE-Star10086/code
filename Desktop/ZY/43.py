favorite_places={"a":["US","UK"],"b":["China"],"c":["Paris","US","Roman"]}
for name,places in favorite_places.items():
    print(f"\n{name}最喜欢的地方是：")
    for place in places:
        print(f"{place}")