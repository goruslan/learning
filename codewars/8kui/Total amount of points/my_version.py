
def points(games):
	point = 0
	for n in range(len(games)):
		if games[n][0] > games[n][-1]:
			point += 3
		elif games[n][0] < games[n][-1]:
			point += 0
		elif games[n][0] == games[n][-1]:
			point += 1
	return point


games = ['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']
points(games)