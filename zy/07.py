respect_people=["Kobe Bryant","Curry","KD"]
respect_people[2]="James"
respect_people.insert(0,"WS")
respect_people.insert(2,"JJK")
respect_people.append("JJboy")
print(f"发现一张大桌子可以容纳嘉宾有：{respect_people}")
print(f"不好意思只能容纳两个人")
unpesent=respect_people.pop()
print(f"{unpesent}先生抱歉，无法邀请您共进晚餐")
print(respect_people)
unpesent=respect_people.pop()
print(f"{unpesent}先生抱歉，无法邀请您共进晚餐")
print(respect_people)
unpesent=respect_people.pop()
print(f"{unpesent}先生抱歉，无法邀请您共进晚餐")
print(respect_people)
unpesent=respect_people.pop()
print(f"{unpesent}先生抱歉，无法邀请您共进晚餐")
print(respect_people)
print(f"{respect_people}先生，您依然在列")
del respect_people[0]
print(respect_people)
del respect_people[0]
print(respect_people)
