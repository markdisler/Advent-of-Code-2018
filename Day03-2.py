from sys import stdin

locs = dict()
id_overlaps = dict()

for line in stdin:

	toks = line.split(' ')
	pos = [int(p) for p in toks[2][:-1].split(',')]
	size = [int(s) for s in toks[3].split('x')]
	id = int(toks[0][1:])

	# initialize the number of overlaps for each claim id
	if not id in id_overlaps:
		id_overlaps[id] = 0

	for x in range(pos[0], pos[0] + size[0]):
		for y in range(pos[1], pos[1] + size[1]):
			p = (x, y)
			if p in locs:
				arr = locs[p]

				# check if this is an overlapping claim id
				# if so, update the overlap counts for both claim ids
				# 'id' is the current id and 'arr[1]' is the last claim id that was read for that location
				if id != arr[1]:
					if id in id_overlaps:
						id_overlaps[id] += 1
					if arr[1] in id_overlaps:
						id_overlaps[arr[1]] += 1

				locs[p] = [arr[0] + 1, id]	# increment count at this point and update the id for overlaps
			else:
				locs[p] = [1, id] # store count and the claim id

print(id_overlaps)

# Find the key that corresponds to no overlaps
for key in id_overlaps.keys():
	if id_overlaps[key] == 0:
		print(key)
		break
