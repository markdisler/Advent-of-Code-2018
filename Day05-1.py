import readline

line = input()
did_react = True
while did_react:
	did_react = False

	i = 0
	while i < len(line) - 1:
		c1 = line[i]
		c2 = line[i + 1]
		if (c1.upper() == c2.upper()) and ((c1.isupper() and c2.islower()) or (c1.islower() and c2.isupper())):
			print('Conflicting: ' + c1 + c2)
			line = line.replace(c1 + c2, '')
			did_react = True
		i += 1

print (len(line))
