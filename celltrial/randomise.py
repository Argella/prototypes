import random
import math

number = 10

victims = [i for i in range(1,number+1)] # number assignment: dict(alice=1, bob=2, carl=3...)


def purge(l, bad):
	for i in bad:
		l.remove(i)


def makegroups(l, n):
	groups = []

	for count in range(n,0,-1):
		groups.append(random.sample(l, int(math.floor(len(l)/count))))
		purge(l, groups[n-count])

	return groups


def getgroup(v, groups):
	for i in range(len(groups)):
		if v in groups[i]:
			return i


