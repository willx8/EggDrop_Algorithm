import random
import math
import egg_drop
from egg_skeleton import EggDropError

class EggDropTest():
    def __init__(self):
        self.rand_upper_bound = 100
        self.rand_lower_bound = 2

    def test_all(self):
        self.test0()
        self.test1()
        self.test2()
        self.test3()
        self.test4()

    def tune(self, lower, upper):
        self.rand_lower_bound = lower
        self.rand_upper_bound = upper

    def para_generator(self):
        N = random.randint(self.rand_lower_bound, self.rand_upper_bound)
        T = random.randint(1, N)
        return T, N

    def test0(self):
        self.test(version=0,
                  max_eggs_func=lambda T, N : 1,
                  max_tosses_func=lambda T, N : N)

    def test1(self):
        self.test(version=1,
                  max_eggs_func=lambda T, N : int(math.ceil(math.log(N, 2))), # IMPORTANT: ROUND UP!
                  max_tosses_func=lambda T, N : int(math.ceil(math.log(N, 2))))

    def test2(self):
        self.test(version=2,
                  max_eggs_func=lambda T, N : max(1, int(math.ceil(math.log(T, 2)))), # Eggs should be at least 1.
                  max_tosses_func=lambda T, N : 2*(max(1, int(math.ceil(math.log(T, 2))))))

    def test3(self):
        self.test(version=3,
                  max_eggs_func=lambda T, N : 2,
                  max_tosses_func=lambda T, N : 2*(int(math.ceil(math.sqrt(N)))))

    def test4(self):
        self.tune(3, 10000000)
        self.test(version=4,
                  max_eggs_func=lambda T, N:2,
                  max_tosses_func=lambda T, N: 3*int(math.ceil(math.sqrt(T))))

    def test(self, version, max_eggs_func, max_tosses_func):
        if not hasattr(egg_drop.EggDrop, "version"+str(version)):
            print "You have not implemented version", version, "yet!"
            return
        else:
            print "Start testing version", version, "...",
        total_tests=100
        for i in range(total_tests):
            T, N = self.para_generator()
            max_eggs = max_eggs_func(T, N)
            max_tosses = max_tosses_func(T, N)
            eggdrop = egg_drop.EggDrop(T, N, max_eggs, max_tosses)
            try:
                result = getattr(eggdrop, "version"+str(version))()
                if result != T:
                    print "\nWrong answer! Expect", T, "Got", result,
                    print "FAIL: T =", T, "N =", N
                    break
            except NotImplementedError:
                print "\nYou have not implemented version", version, "yet!"
                return
            except EggDropError as e:
                print "\nError occur:", e.msg,
                print "FAIL: T =", T, "N =", N
                return
        print "OK"


def main():
    test = EggDropTest()
    test.test_all()

if __name__ == "__main__":
    main()