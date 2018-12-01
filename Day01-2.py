flist = list()
line = input()
while line != '':
	flist.append(int(line))
	line = input()

v = 0
visited = set()
visited.add(v)
i = 0
while True:
	v += flist[i % len(flist)]
	if v in visited:
		print(v)
		break

	visited.add(v)
	i += 1
