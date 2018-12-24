all_ids = list()

line = input()
while line != '':
	all_ids.append(line)
	line = input()

for x in all_ids:
	for y in all_ids:
		if x != y:
			num_diff = 0
			for i in range(0, len(x)):
				if x[i] != y[i]:
					num_diff += 1

			if num_diff == 1:
				print(x, y)
