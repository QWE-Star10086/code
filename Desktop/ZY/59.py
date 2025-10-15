def make_album(name,thing):
    things={"singer":name,"sing":thing}
    return things
while True:
    print(f"\n请输入你的专辑信息：")
    NAME=input("姓名:")
    if NAME=='quit':
        break
    THING=input("专辑:")
    if THING=='quit':
        break
    music=make_album(NAME,THING)
    print(music)
