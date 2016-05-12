import re
import sys
f = open(sys.argv[1])
for line in f:
	lineC = re.split('[()]',line)
	last = " "
	level = 0
	for c in lineC:
		if c == "" :
			if last == " ":
				level += 1
			else:
				level -= 1
				if level < 0:
					level = 0
		elif c == " ":
			level = level
		else:
			for x in range(0,level):
				sys.stdout.write("\t")
			print c
		last = c
