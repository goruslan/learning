def points2(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))

# or this
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count


games = ['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']
print(points2(games))