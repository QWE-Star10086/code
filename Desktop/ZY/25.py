age=5
if age<2:
    people_type="婴儿"
elif 2<=age<4:
    people_type="幼儿"
elif 4<=age<13:
    people_type="儿童"
elif 13<=age<18:
    people_type="少年"
elif 18<=age<65:
    people_type="中青年人"
else:
    people_type="老年人"
print(f"这个人是{people_type}")