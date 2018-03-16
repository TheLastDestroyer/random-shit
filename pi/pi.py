from random import uniform
from console import clear
r = 1

n = 0
inside = 0
while True:
	for _ in range(100000):
		n += 1
		point = (uniform(-r,r), uniform(-r,r))
		if point[0]**2 + point[1]**2 < 1:
			inside += 1
	pi = inside / n * 4
	clear()
	print(pi)
