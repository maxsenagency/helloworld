import random
import math

iteration = 1000000
total = 0


x = random.random()
y = random.random()

dist = math.sqrt(x * x + y * y)

print(dist)

for i in range(1,iteration) :
    x = random.random()
    y = random.random()

    dist = math.sqrt(x * x + y * y)

    if dist <= 1:
        total+=1

pi = total / iteration * 4

print(pi)
