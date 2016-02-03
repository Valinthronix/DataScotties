from SnakesLadders import *
import pprint

game = GameFSM(16)

# Make ladders
game.all_states[2].set(10)
game.all_states[8].set(14)

# Make snakes
game.all_states[11].set(4)
game.all_states[15].set(6)

data = []

RUNS = 1000

for i in range(RUNS):
	game.run()
	moves = count_moves(game.records)
	snl = count_snakes_and_ladders(game.records)
	data.append({'moves': moves, 'snakes': snl[0], 'ladders': snl[1]})
	game.reset()

pprint.pprint(data)

def avg(cat):
    sum = 0
    for i in range(RUNS):
        sum += data[i][cat]
    return (sum/RUNS)
