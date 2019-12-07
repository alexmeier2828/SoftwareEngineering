class ScoreKeeper:
    def __init__(self):
        self.score = 0
        self.combo = 0

    #increment score by a factor of size.  Score is modified by combo
    #counter. Incrementing the score will increment the combo counter.
    def increment(self, size):
        self.score += size * (self.combo + 1)
        self.combo += 1
        print(str(self.combo))

    #resets the combo counter
    def endCombo(self):
        self.combo = 0
