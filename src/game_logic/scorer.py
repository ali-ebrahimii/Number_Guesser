
class Scorer:
    def __init__(self, inital_score=100):
        self.score = inital_score
    
    def decrement_score(self, penalty=10):
        """Decrease the score by a certain penalty."""
        self.score -= penalty
        self.score = max(self.score, 0)
    
    def get_score(self):
        """Return the current score."""
        return self.score
        