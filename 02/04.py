from sys import argv
from collections import defaultdict
data = open(argv[1]).read().strip()
sum = 0
for line in data.split('\n'):
    game = line.split(':')[1]
    val = defaultdict(int)
    for selection in game.split(';'):
        for balls in selection.split(','):
            num,colour = balls.split()
            val[colour] = max(val[colour],int(num))
    power = 1
    for v in val.values():
        power *= v
    sum += power
print(sum)
