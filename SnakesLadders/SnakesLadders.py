from random import randint
import pprint

class State(object):
    def __init__(self, ix):
        self.index = ix
        self.link = None  # placeholder, not None if Snake or Ladder

    def process(self):
        """Action when landed upon"""
        if self.link:
            if self.link > self.index:
                # Ladder!
                return self.link
            else:
                # Snake!
                return self.link
        else:
            # link is None: "Normal" = not a snake or ladder
            return self.index

def roll(): return randint(1,6)

class GameFSM(object):
    def __init__(self, n):
        self.all_states = []
        self.position = 0
        self.n = n 
        for ix in range(n+1):
            self.all_states.append(State(ix))
        self.history = (None, None)
        for i in self.history:
            i = []
            
    def move(self, die):
        """die is an integer
        """
        self.history[0].append(die)
        inter_pos = self.position + die
        state_obj = self.all_states[inter_pos]
        final_pos = state_obj.process()
        self.position = final_pos
        self.history[1].append(self.position)
        
    def run(self):
        print("Starting game!")
        while self.position < self.n:
            # roll die
            die = roll()
            # move based on die roll
            self.move(die)
            # record results
        print("Game over!")
        
    def story(self):
        pprint.pprint(self.history)
        
game = GameFSM(16)

print(game.all_states)

# Ladders

game.all_states[2].link = 10
game.all_states[8].link = 14

