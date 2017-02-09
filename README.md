# Water-Jug

# This Program tackles the water-jug problem.  The premise is simple, you are given 3 numbers, the first two represent the size of 2 jugs, and the 3rd is the goal state of the larger jug.
# 3 operations exist, fill a jug, empty a jug, or transfer from one to the other
# With these three operators, the goal state must be achieved, in the case of our usage, in 50 moves or less.
# As an example...4 3 2...meaning you have a 4 liter jug, a 3 liter jug, and the goal at the end is to have 2 liters of water present in the 4 liter jug.
# The printed results is the history, denoting the way the goal was achieved.
# The program is executed by breadth first search, not depth first.  This is absolutely vital, because without this the problem becomes a brute force search, which with 50 itterations, and 3 operations, total number of permutations is 3^(50) = 717,897,987,691,852,588,770,249.
