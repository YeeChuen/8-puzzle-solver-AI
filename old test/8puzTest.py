
from importlib.resources import contents
from re import A
import sys  #sys is not used, using argparse instead
import argparse
from time import time
from turtle import up
from unittest import result
from searchTest import *

#Author: Yee Chuen Teoh
#Title: COM S 572 Lab 1

#learn how to take commandline argument
'''
sys.argv is a function that read arguments after python file.py 1 2 3 , 
sys.argv[0] = file.py
sys.argv[1] = 1
sys.argv[2] = 2
sys.argv[3] = 3
detail information on https://www.geeksforgeeks.org/command-line-arguments-in-python/
'''
#with open(sys.argv[1], 'r') as f:
#   contents = f.read()

#learn how to take commandline argument as name
'''
uses argparse

#create parser
parser = argparse.ArgumentParser()
#add parser argument --fPath and --alg
parser.add_argument('--fPath', type=str, required=True)
parser.add_argument('--alg', type=str, required=True)
#parse the argument
args = parser.parse_args()
print("---------------------------------------------------")
'''


#curr location in 8 puzz, to be manipulate
#key is actual location in goal state
state = "_23785461"

dist = {"1":"012123234", "2":"101212323", "3":"210321432", "4":"123012123", "5":"212101212", 
        "6":"321210321", "7":"234123012", "8":"323212101", "_":"432321210"}  
heuristic = 0
for x in state:
    goal = dist[x]
    heuristic = heuristic+int(goal[state.find(x)])
    print(x + " is in " +str(state.find(x)))
    print(x + " has distance of " +(goal[state.find(x)]))

test = heuristic
state= state.replace("_","9")
print(state)
for x in state:
    lookForStr = int(state.find(x)) +1
    check = int(x) -1
    if int(state[check]) == int(x):
        continue
    if int(state[check]) == lookForStr:
        txt = "this two {} and {} are in reversal"
        print(txt.format(x,state[check]))
        test+=1
state= state.replace("9","_")
print(state)
print(heuristic)
print(test)


#old practice code below
'''
print("practice zone")
algo = args.alg
print("Filename: "+ contents)
print("Algorithm: "+ algo)
contents = args.fPath
puzzlefile = open(contents)
puzzle = puzzlefile.read()
a = puzzle.replace(" ","")
initialstate = a.replace("\n","")
print(puzzle)
print(type(puzzle))

print("---------------------------------------------------")
#TOBE DELETED
# contents to be deleted
print("SOLVABLE")
print("total nodes generated: ")
print("Total time taken: ")
print("Path length: ")
print("Path: ")
print(" ")
print("UNSOLVABLE")
print("The inputted puzzle is not solvable:")    
print(puzzle)
print("---------------------------------------------------")

'''
'''
Lab 1 start Problem Formulation
States: all possible combination of 9 spaces
Initital State: any txt file
Action: ("Up", "Down", "Left", "Right")
Goal test: state equal to SGoal.txt
Action cost: 1 per action
'''
'''
print("test compiler")
print(" ")

goalfile = open("SGoal.txt")
goal = goalfile.read()
b = goal.replace(" ","")
goalstate = b.replace("\n","")
i = "12345_678"
problem = Problem(i, goalstate)

print("---------------------------------------------------")
print("test action")
print(" ")
problem.actions(initialstate)

print("---------------------------------------------------")

print("test result")
print(" ")
problem.result(initialstate, "Up")
print(" ")
problem.result(initialstate, "Down")
print(" ")
problem.result(initialstate, "Left")
print(" ")
problem.result(initialstate, "Right")

print("---------------------------------------------------")

print("TODO Task:")
print("1. BFS")
print("2. IDS (Iterative deepening DFS)")
print("3. A* with misplaced title heuristic. (h1)")
print("4. A* with Manhattan distance heuristic (h2)")
print("5. A* with one more heuristic (invent or check the literature for this) (h3)")

print("---------------------------------------------------")
print("1. BFS") 
starttime = time.time()
BFStest = breadth_first_graph_search(problem)
endtime = time.time()

print("---------------------------------------------------")
print("result")
print(" ")
print("Start time: "+str(starttime))
print("End time: "+str(endtime))
print(" ")
print(">---<Requirement print>---<")
print(" ")
print("Initial State: " +i)
print("Final State: " +BFStest.state)
print("Elapsed time: " + str(endtime-starttime)+"seconds")
print("Path Cost: "+ str(BFStest.path_cost))
print(BFStest.solution())
print(" ")
print(">---<Requirement print>---<")
print("---------------------------------------------------")
print("2. IDS") 
starttime = time.time()
IDStest = iterative_deepening_search(problem)
endtime = time.time()
print("---------------------------------------------------")
print("result")
print(" ")
print("Start time: "+str(starttime))
print("End time: "+str(endtime))
print(" ")
print(">---<Requirement print>---<")
print(" ")
print("Initial State: " +i)
print("Final State: " +IDStest.state)
print("Elapsed time: " + str(endtime-starttime)+"seconds")
print("Path Cost: "+ str(IDStest.path_cost))
print(IDStest.solution())
print(" ")
print(">---<Requirement print>---<")
print("---------------------------------------------------")
print("3. A* with misplaced title heuristic. (h1)") 

eightpuz = EightPuzzle((5,3,1,0,8,7,2,6,4))
starttime = time.time()
Astar = astar_search(eightpuz, None, False)
endtime = time.time()
print("---------------------------------------------------")
print("result")
print(" ")
print("Start time: "+str(starttime))
print("End time: "+str(endtime))
print(" ")
print(">---<Requirement print>---<")
print(" ")
print("Initial State: " +i)
print("Final State: " + str(Astar.state))
print("Elapsed time: " + str(endtime-starttime)+"seconds")
print("Path Cost: "+ str(Astar.path_cost))
print(Astar.solution())
print(" ")
print(">---<Requirement print>---<")
print("---------------------------------------------------")
print("4. A* with Manhattan distance heuristic (h2)") 

eightpuz = EightPuzzle((5,3,1,0,8,7,2,6,4))
starttime = time.time()
Astar = PlanRoute(eightpuz, None, False)
endtime = time.time()
print("---------------------------------------------------")
print("result")
print(" ")
print("Start time: "+str(starttime))
print("End time: "+str(endtime))
print(" ")
print(">---<Requirement print>---<")
print(" ")
print("Initial State: " +i)
print("Final State: " + str(Astar.state))
print("Elapsed time: " + str(endtime-starttime)+"seconds")
print("Path Cost: "+ str(Astar.path_cost))
print(Astar.solution())
print(" ")
print(">---<Requirement print>---<")
'''