from sys import stdin

# take input and sort it
entry_strings = list()
for line in stdin:
	entry_strings.append(line[:-1])
entry_strings = sorted(entry_strings)

sleep_time = dict()
current_guard = 0
begin = 0
for line in entry_strings:

	observation = line[line.index(']')+2 :]
	min = int(line.split(' ')[1].split(':')[1][:-1])

	if observation.startswith('Guard'):
		current_guard = int(observation.split(' ')[1][1:])
		if not current_guard in sleep_time:
			sleep_time[current_guard] = 0
	elif observation == 'falls asleep':
		begin = min
	elif observation == 'wakes up':
		end = min
		sleep_time[current_guard] += end - begin

max_guard = max(sleep_time, key=sleep_time.get)

minutes_for_guard = dict()
for i in range(0, 60):
	minutes_for_guard[i] = 0

current_guard = 0

for line in entry_strings:

	observation = line[line.index(']')+2 :]
	min = int(line.split(' ')[1].split(':')[1][:-1])

	if observation.startswith('Guard'):
		current_guard = int(observation.split(' ')[1][1:])
	elif observation == 'falls asleep':
		begin = min
	elif observation == 'wakes up' and current_guard == max_guard:
		end = min
		for j in range(begin, end):
			minutes_for_guard[j] += 1

max_minute = max(minutes_for_guard, key=minutes_for_guard.get)
print(max_guard)
print(max_minute)
print(max_guard * max_minute)
