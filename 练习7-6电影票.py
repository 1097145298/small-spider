# 电影票
age = "请输入年龄:"
note = ""
active = True
while active:
    note = input(age)
    if note != 'quit':
        note = int(note)
        if note < 3:
            print("免费")
        elif note <= 12:
            print("12美元")
        else:
            print("15美元")
    else:
        break
