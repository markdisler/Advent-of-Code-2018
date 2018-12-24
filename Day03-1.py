from sys import stdin

locs = dict()

for line in stdin:

	toks = line.split(' ')
	pos = [int(p) for p in toks[2][:-1].split(',')]
	size = [int(s) for s in toks[3].split('x')]

	for x in range(pos[0], pos[0] + size[0]):
		for y in range(pos[1], pos[1] + size[1]):
			p = (x, y)
			if p in locs:
				locs[p] += 1
			else:
				locs[p] = 1


# Count up positions with >= 2 claims
count = 0
for v in locs.values():
	if v >= 2:
		count += 1
print(count)
