def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

print(abbrevName("Sam Harris"))