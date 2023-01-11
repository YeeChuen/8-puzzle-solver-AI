#Author: Yee Chuen Teoh
#Title: COM S 572 Lab 1
#Reference: Search (Chapters 3-4) textbook Artificial Intelligence_ A Modern Approach

import argparse
from time import time
from Pformulation import *
from search import *
import time
import glob

#choose time limit for each algo
'''Edit minimum time here
currently set at 10'''
mintime = 900

'''
NOTES
- makesure mintime is 900 for 15min max
'''

#create parser
parser = argparse.ArgumentParser()
#add parser argument --fPath and --alg and --alltxt

#choose a txt file to run, needs to be in same folder
#example --fPath S1.txt
#type all to run all txt file
parser.add_argument('--fPath', type=str, required=True)

#choose a algorithm to run
#example --alg BFS/IDS/h1/h2/h3
#type all to run all 5 algorithm, --alg all
parser.add_argument('--alg', type=str, required=True)

#parse the argument
args = parser.parse_args()

#check what algo is asked to run
algo = args.alg

#have a global dict to track total runtime and total generated node
#key: algorithm name (BFS/IDS/h1/h2/h3)
#value: list of [totalruntime, totalgenerated node, successrun]
dict = {"BFS":[0,0,0], "IDS":[0,0,0],"h1":[0,0,0],"h2":[0,0,0],"h3":[0,0,0], "h4":[0,0,0]}

#printresult function to help printing
def printresult(search, starttime, algo, hidedetail):
    endtime = time.time()

    #if cant find a solution, 8puz typically will have solution
    #if solvability is true
    if search == None:
        if hidedetail == False:
            print("search algo failed")
            print("")
            return
        

    #only if the state says "Timed out", it meant that the algorithm takes too long
    elif search.state == "Timed out.":
        if hidedetail == False:
            print("Total nodes generated: <<??>>")
            print("Total time taken: >15 min")
            print("Path length: "+search.state)
            print("Path: "+search.state)
            print("")
            return

    #prints detail of algorithm
    else:
        dict[algo][2]+=1
        if hidedetail == False:
            print("Total nodes generated: "+str(search.nodeNum))
            print("Total time taken: "+str(round(endtime-starttime, 5))+" seconds")
            print("Path length: "+str(search.path_cost))
            print("Path: "+''.join(search.solution()))
            print("")

        
        #dict[algo][0] represent total runtime
        dict[algo][0]+=round(endtime-starttime, 5)
        #dict[algo][1] represent total generated node
        dict[algo][1]+=search.nodeNum

#a function that only print final average result.
#show what files are ran
#then show algorithm that is used. and their average
def printavgresult(algo, numtest):
    totaltest = numtest
    totalpass = 0
    for key in dict:
        totalpass+=dict[key][2]
    if algo == "all":
        totaltest*=len(dict)

    print("")
    print(str(totalpass) + "/" + str(totaltest) + "successfully run")
    print("")

    if totalpass == 0:
        return
    #average algo serve to print the average result
    def average(algo):
        title = "Average result of {} ---------------------- {}"
        print(title.format(algo,algo))
        success = "| {}/{} success"
        print(success.format(dict[algo][2],numtest))
        print("| Average run time: " + str(round(dict[algo][0]/dict[algo][2],5)))
        print("| Average node explored: " + str(round(dict[algo][1]/dict[algo][2], 1)))
        print("----------------------------------------------")
        print("")

    if algo != "all":
        average(algo)

    else: 
        algoList = ["BFS", "IDS", "h1", "h2", "h3", "h4"]
        for x in algoList:
            average(x)

#runtest function runs the .txt files, using algo, if algo == all, run all 5 algo
def runtest(contents, algo, hidedetail):
    puzzlefile = open(contents, "r")
    puzzle = puzzlefile.read()
    a = puzzle.replace(" ","")
    initialstate = a.replace("\n","")
    #create the problem using initial state
    problem = EightPuzzle(initialstate)

    #check problem solvability
    print("")
    print("txt file("+ contents +") solvability = "+str(problem.check_solvability(initialstate)))
    print("")

    if not problem.check_solvability(initialstate):
        print("The inputted puzzle is not solvable:")
        print(puzzle)

    else:
        #check input algo is valid, if not, print not valid
        valid = 0

        #BFS
        if algo == "BFS" or algo == "all":
            starttime = time.time()
            print("--- running "+contents+" puzzle on BFS ---")
            printresult(breadth_first_graph_search(problem, starttime, mintime), starttime, "BFS", hidedetail)
            valid+=1

        #IDS
        '''
        note: nodes generated in IDS is much higher
        as nodes in every depth limit is counted as generated,
        and not just only when the solution is found.
        '''
        if algo == "IDS" or algo == "all":
            starttime = time.time()
            print("--- running "+contents+" puzzle on IDS ---")
            printresult(iterative_deepening_search(problem, starttime, mintime), starttime, "IDS", hidedetail)
            valid+=1

        #h1
        if algo == "h1" or algo == "all":
            starttime = time.time()
            print("--- running "+contents+" puzzle on h1 ---")
            problem = EightPuzzleH1(initialstate)
            printresult(astar_search(problem, starttime, mintime), starttime, "h1", hidedetail)
            valid+=1

        #h2
        if algo == "h2" or algo == "all":
            starttime = time.time()
            print("--- running "+contents+" puzzle on h2 ---")
            problem = EightPuzzleH2(initialstate)
            printresult(astar_search(problem, starttime, mintime), starttime, "h2", hidedetail)
            valid+=1

        #h3
        if algo == "h3" or algo == "all":
            starttime = time.time()
            print("--- running "+contents+" puzzle on h3 ---")
            problem = EightPuzzleH3(initialstate)
            printresult(astar_search(problem, starttime, mintime), starttime, "h3", hidedetail)
            valid+=1

        #h4
        if algo == "h4" or algo == "all":
            starttime = time.time()
            print("--- running "+contents+" puzzle on h4 ---")
            problem = EightPuzzleH4(initialstate)
            printresult(astar_search(problem, starttime, mintime), starttime, "h4", hidedetail)
            valid+=1

        #valid = 0 indicate algo is not valid
        if valid==0:
            print("algorithm for --algo is not valid")
            print("please input one of the following after --algo:")
            print("--algo (BFS/IDS/h1/h2/h3/h4/all)")
            print("note* add '*' at the end to only show average result on algorithm ")
            print("      add '**' at the end to show both detail and average result on algorithm ")
            print("")

#get the txt file, convert to initialstate form
contents = args.fPath

print("")
print("--- Start test ---")
#here check algo has * at the end, if yes, hidedetail = true
#if algo has ** at the end, hideaverage = true
hidedetail = False
hideaverage = True
if algo.endswith('**'):
    hideaverage = False
    algo=algo.replace("*","")
elif algo.endswith('*'):
    hidedetail = True
    hideaverage = False
    algo=algo.replace("*","")

detail = "test status: hidedetail: {}, hideaverage: {}"
print(detail.format(str(hidedetail),str(hideaverage)))
print("")




#here check if the fPath ends with .txt (since Part1 Lab1 require input path)
#if yes, means there is only 1 file to run, else, assume its a folder
numtest = 1
if contents.endswith('.txt'):
    runtest(contents, algo, hidedetail)
else:
    folder=contents
    folder = folder+"/*.txt"
    txt_files=glob.glob(folder)
    #number of test
    numtest = len(txt_files)
    #loop through all the txt_files
    for x in txt_files:
        runtest(x, algo, hidedetail)

if hideaverage == False:
    printavgresult(algo, numtest)

print("")
print("--- End test ---")
print("")
