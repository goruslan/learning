def abbrevName(name):
    name = name.upper().split(" ")
    initials = name[0][0]+'.'+name[1][0]
    return initials


print(abbrevName("Sam Harris"))