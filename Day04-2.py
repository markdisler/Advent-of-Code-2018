from sys import stdin
from collections import Counter

# take input and sort it
entry_strings = list()
for line in stdin:
	entry_strings.append(line[:-1])
entry_strings = sorted(entry_strings)

ids_list = list()  # all guards
sleep_time = dict() # guard : list of mins where they were asleep
current_guard = 0
begin = 0
for line in entry_strings:

	observation = line[line.index(']')+2 :]
	min = int(line.split(' ')[1].split(':')[1][:-1])

	if observation.startswith('Guard'):
		current_guard = int(observation.split(' ')[1][1:])
		if not current_guard in sleep_time:
			sleep_time[current_guard] = list() # list of mins
			ids_list.append(current_guard)
	elif observation == 'falls asleep':
		begin = min
	elif observation == 'wakes up':
		end = min
		for i in range(begin, end):
			sleep_time[current_guard].append(i)

# Get mode for each guard and compare num of occurances
guard_id = 0
most_common = 0
count = 0
for i in ids_list:
	if len(sleep_time[i]) == 0: continue

	counter = Counter(sleep_time[i])
	mc = counter.most_common(1)[0] #[(mode, occ)] => (mode, occ)
	occurrances = mc[1]

	if occurrances > count:
		most_common = mc[0]
		count = occurrances
		guard_id = i

print(str(guard_id) + ' * ' + str(most_common) + ' = ' + str(guard_id * most_common))
