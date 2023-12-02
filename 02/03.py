from sys import argv
data = open(argv[1]).read().strip()
sum = 0
max = {'red': 12, 'green': 13, 'blue': 14}
for line in data.split('\n'):
    allowed = True
    game_id,game = line.split(':')
    game_num = game_id.split()[1]
    for selection in game.split(';'):
        for balls in selection.split(','):
            num,colour = balls.split()
            if int(num) > max.get(colour):
                allowed = False
    if allowed:
        sum += int(game_num)
print(sum)
