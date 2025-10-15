favourites_language={
    "jen":"java",
    "jjk":"python",
    "hen":"c",
    "susan":"rust"
    }
names=["jen","jjk","hen","susan","bbg","ook"]
for name in names:
    if name in favourites_language.keys():
        print(f"{name}，感谢您的参加")
    else:
        print(f"{name},诚邀您来参加")