pets={
    "dog":{
        "name":"jjk",
        "user":"susan"
    },
    "cat":{
        "name":"ook",
        "user":"younger"
    },
}
for pet,pet_info in pets.items():
    print(f"\npettype:{pet}")
    Name=pet_info["name"]
    Home=pet_info["user"]
    print(f"\npetname:{Name}")
    print(f"\nHomeUser:{Home}")