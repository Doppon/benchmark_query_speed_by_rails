import random

path = 'seed.txt'
data = int( random.uniform(1.0, 50000.0) )

with open(path, mode='w') as f:
    f.write(str(data))
