#Author: Yee Chuen Teoh
#Title: COM S 572 Lab 1
#Reference: Search (Chapters 3-4) textbook Artificial Intelligence_ A Modern Approach

import argparse
from time import time
from Pformulation import *
from search import *
import time

initial = "531_87264"
#initial = "12345_678"
#S1.txt
#initial = "352617_84"
problem = EightPuzzle(initial)
solvable = ""
if problem.check_solvability:
    solvable = "true"
else: 
    solvable = "false"

print("---------------------------------------------------")
#BFS
starttime = time.time()
BFSrun = breadth_first_graph_search(problem, starttime)
endtime = time.time()

print("Algorithm: Breaadth First Graph Search")
print("Puzzle solvability: "+ solvable)
print("Initial state: "+initial)
print("Final state: "+BFSrun.state)
print("Start time: "+str(starttime)+"seconds")
print("End time: "+str(endtime)+"seconds")
print("Total node generated: "+str(BFSrun.nodeNum))
print("Total time taken: "+str(endtime-starttime)+"seconds")
print("Path length: "+str(BFSrun.path_cost))
print("Path: "+''.join(BFSrun.solution()))
print("---------------------------------------------------")
#IDS
starttime = time.time()
IDSrun = iterative_deepening_search(problem, starttime)
endtime = time.time()

print("Algorithm: Iterative Deepening Search")
print("Puzzle solvability: "+ solvable)
print("Initial state: "+initial)
print("Final state: "+IDSrun.state)
print("Start time: "+str(starttime)+"seconds")
print("End time: "+str(endtime)+"seconds")
print("Total node generated: "+str(IDSrun.nodeNum))
print("Total time taken: "+str(endtime-starttime)+"seconds")
print("Path length: "+str(IDSrun.path_cost))
print("Path: "+''.join(IDSrun.solution()))
print("---------------------------------------------------")

#misplaced tile heuristic

#uses EightPuzzleH1 which contains misplaced tiles heuristic
problem = EightPuzzleH1(initial)

starttime = time.time()
Astarrun = astar_search(problem, starttime)
endtime = time.time()


print("Algorithm: A* with misplaced title heuristic (h1)")
print("Puzzle solvability: "+ solvable)
print("Initial state: "+initial)
print("Final state: "+Astarrun.state)
print("Start time: "+str(starttime)+"seconds")
print("End time: "+str(endtime)+"seconds")
print("Total node generated: "+str(Astarrun.nodeNum))
print("Total time taken: "+str(endtime-starttime)+"seconds")
print("Path length: "+str(Astarrun.path_cost))
print("Path: "+''.join(Astarrun.solution()))
print("---------------------------------------------------")

#Manhattan heuristic

#uses EightPuzzleH2 which contains Manhattan heuristic
problem = EightPuzzleH2(initial)

starttime = time.time()
Astarrun2 = astar_search(problem, starttime)
endtime = time.time()


print("Algorithm: A* with manhattan heuristic (h2)")
print("Puzzle solvability: "+ solvable)
print("Initial state: "+initial)
print("Final state: "+Astarrun2.state)
print("Start time: "+str(starttime)+"seconds")
print("End time: "+str(endtime)+"seconds")
print("Total node generated: "+str(Astarrun2.nodeNum))
print("Total time taken: "+str(endtime-starttime)+"seconds")
print("Path length: "+str(Astarrun2.path_cost))
print("Path: "+''.join(Astarrun2.solution()))

print("---------------------------------------------------")

#Custom heuristic

#uses EightPuzzleH2 which contains CUstom heuristic
problem = EightPuzzleH3(initial)

starttime = time.time()
Astarrun3 = astar_search(problem, starttime)
endtime = time.time()


print("Algorithm: A* with Custom heuristic (h3)")
print("Puzzle solvability: "+ solvable)
print("Initial state: "+initial)
print("Final state: "+Astarrun3.state)
print("Start time: "+str(starttime)+"seconds")
print("End time: "+str(endtime)+"seconds")
print("Total node generated: "+str(Astarrun3.nodeNum))
print("Total time taken: "+str(endtime-starttime)+"seconds")
print("Path length: "+str(Astarrun3.path_cost))
print("Path: "+''.join(Astarrun3.solution()))

#TO DO
# CHECKED generate nodes
# CHEKCED if search algo go to repeated state, node check visited before opening or is it in fringe?
# CHECKED how to keep track of time in real time.
