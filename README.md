# EggDrop_Algorithm


## Introduction

With the code provided, you can:

- Focus on writing codes for each version without checking whether eggs or tosses has been used up, which pollutes your code.

- Stop worrying about the test, cuz it's been taken care of by the test & skeleton.

- Expand more version easily if you like: all the limitations in test.py is written in lambda so just write formula and you can expand it.


## The Problem

These python files are intended to help when solving the algorithm problem ***Egg Drop***:

> Suppose that you have an N-story building and plenty of eggs.
  An egg breaks if it is dropped from floor T or higher and does not break otherwise.
  Your goal is to devise a strategy to determine the value of T given the following
  limitations on the number of eggs and tosses:
  
> Version 0: 1 egg, <= T tosses.

> Version 1: logN eggs and logN tosses.

> Version 2: logT eggs and 2logT tosses.

> (Advanced)Version 3: 2 eggs and 2*N^(1/2) tosses.

> (Advanced)Version 4: 2 eggs and <= c*T^(1/2) tosses for some fixed constant c.


## How To Use The Code

### 1. Git clone it.

### 2. Implement methods in `egg_drop.py`

*NOTE: you don't have to change codes in `egg_skeleton.py` and `test.py`.*

### 3. Run `test.py`

```
> python test.py
```

You will get informations about each version on:

- You've not implemented the version yet.

- The eggs' been used up

- The tosses' been used up

- Your function yields wrong answer.

If none, you will see:

```
Start testing version 0 ... OK
Start testing version 1 ... OK
Start testing version 2 ... OK
Start testing version 3 ... OK
Start testing version 4 ... OK
```
**Then congratulations, you are done!**

If any error occures, just fix them and rerun.

*P.S: I go with 3 for the constant c in version 4, which is enough for my implementation. However you may edit that constant in `test.py`.*

---

<a href="https://github.com/willx8/egg-drop-solution/blob/master/egg_drop.py">Here is my implementation of all 5 versions of the algorithm </a>.

ENJOY!
