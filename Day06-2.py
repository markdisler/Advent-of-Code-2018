from sys import stdin

initialLocs = list()
grid = dict()
letter = 'A'
min_x = min_y = max_x = max_y = -1
for line in stdin:
	coord = line[:-1].split(', ')
	x, y = int(coord[0]), int(coord[1])
	initialLocs.append((x, y, letter))
	grid[(x, y)] = letter
	letter = chr(ord(letter) + 1) #incr letter

	# Assign bounds
	max_x = max(max_x, x)
	max_y = max(max_y, y)
	min_x = x if min_x < 0 else min(min_x, x)
	min_y = y if min_y < 0 else min(min_y, y)

# Fill the region
for j in range(min_y, max_y + 1):
	for i in range(min_x, max_x + 1):
		total_dist = 0
		for c in initialLocs:
			total_dist += abs(c[0] - i) + abs(c[1] - j)

		if total_dist < 10000:
			grid[(i, j)] = '#'
		else:
			grid[(i, j)] = '.'

# Get region size
grid_vals = list(grid.values())
region_size = grid_vals.count('#')
print(region_size)
