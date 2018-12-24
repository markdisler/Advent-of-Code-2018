alphabet = [chr(c) for c in range(ord('a'), ord('z') + 1)]

numTwice = 0
numThree = 0

line = input()
while line != '':

	good2 = False
	good3 = False
	for a in alphabet:
		if line.count(a) == 2:
			good2 = True
		if line.count(a) == 3:
			good3 = True

	numTwice += good2
	numThree += good3

	line = input()

print(numTwice * numThree)
