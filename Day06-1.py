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

# Keep track of border letters which indicate infinite areas
borders = set()

# Fill in gaps in grid
for j in range(min_y, max_y + 1):
	for i in range(min_x, max_x + 1):
		if not (i, j) in grid:
			distances = dict()
			for c in initialLocs:
				distances[c[2]] = abs(c[0] - i) + abs(c[1] - j)

			min_key = min(distances, key=distances.get)
			val = distances[min_key]
			min_count = list(distances.values()).count(val)
			grid[(i, j)] = min_key if min_count == 1 else '.'

		if i == min_x or i == max_x or j == min_y or j == max_y:
			if grid[i, j] != '.':
				borders.add(grid[(i, j)]) # track infinite areas

# Get Finite Area letters
all_letters = set([chr(x) for x in range(ord('A'), ord(letter))])
finite_areas = all_letters - borders
print(finite_areas)

# Get max area of finite areas
grid_vals = list(grid.values())
area_sizes = [grid_vals.count(x) for x in finite_areas];
print(max(area_sizes))
