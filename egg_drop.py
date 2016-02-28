import math
import egg_skeleton


class EggDrop(egg_skeleton.EggDropSkeleton):
    """
    Egg drop.
    Suppose that you have an N-story building and plenty of eggs.
    An egg breaks if it is dropped from floor T or higher and does not break otherwise.
    Your goal is to devise a strategy to determine the value of T given the following
    limitations on the number of eggs and tosses:
        Version 0: 1 egg, <= T tosses.
        Version 1: logN eggs and logN tosses. [ROUND UP]
        Version 2: logT eggs and 2logT tosses. [ROUND UP]
        (Advanced)Version 3: 2 eggs and 2*N^(1/2) tosses.
        (Advanced)Version 4: 2 eggs and <= c*T^(1/2) tosses for some fixed constant c.
    """

    # This is a sample implementation. As you can see, the functions are expected to return
    # the value of T. You can access self.N for building height and call self.toss(i) to toss
    # the egg at floor i. The self.toss(i) will return True if the egg is broken, False otherwise.
    # The tosses and eggs you used will be automatically recorded. Infinite eggs and tosses may
    # be assumed. The test will report error if they exceeds the limitation.
    # Of course you can call self.T for the exact value of T, but that'd spoil all the fun, wouldn't it?
    def version0(self):
        floor = 0
        egg_broken = False
        while not egg_broken:
            floor += 1
            egg_broken = self.toss(floor)
        return floor

    def version1(self):
        raise NotImplementedError()

    def version2(self):
        raise NotImplementedError()

    def version3(self):
        raise NotImplementedError()

    def version4(self):
        raise NotImplementedError()