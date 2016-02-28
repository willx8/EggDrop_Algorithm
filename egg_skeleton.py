class EggDropSkeleton:
    def __init__(self, T, N, max_eggs, max_tosses):
        self.T = T # T is min floor where egg breaks
        self.N = N # N is the number of stories a building have.
        self.eggs = max_eggs
        self.tosses = max_tosses

    def toss(self, floor):
        if floor > self.N or floor <= 0:
            raise EggDropError("Toss at illegal floor:"+str(floor))
        self.tosses -= 1
        if self.tosses < 0:
            raise EggDropError("Tosses used up!")
        if floor >= self.T:
            self.eggs -= 1
            if self.eggs < 0:
                raise EggDropError("Eggs used up!")
            return True
        else:
            return False


class EggDropError(Exception):
    def __init__(self, msg):
        self.msg = msg
