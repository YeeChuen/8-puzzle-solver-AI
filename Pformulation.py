#Author: Yee Chuen Teoh
#Title: COM S 572 Lab 1
#Reference: Search (Chapters 3-4) textbook Artificial Intelligence_ A Modern Approach

from ast import Str
import sys
from collections import deque
from tabnanny import check

from utils import *

# ______________________________________________________________________________
# Problem Formulation
class Problem:
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    #set what are the states
    #use string consist of "_012345678" as state
    def __init__(self, initial, goal=None):
        #TO BE DELETED
        #print("start Problem.__init__")
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

        #TO BE DELETED
        #print("initial state: "+self.initial)
        #print("goal state: "+self.goal)

        
        #TO BE DELETED
        #print("end Problem.__init__")

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        #list of available action base on '_' location
        '''
        0 1 2
        3 4 5
        6 7 8
        -----
        0: Down3, Right1
        1: Down4, Left0, Right2
        2: Down5, Left1
        3: Up0, Down6, Right4
        4: Up1, Down7, Left3, Right5
        5: Up2, Down8, Left4
        6: Up3, Right7
        7: Up4, Left6, Right8
        8: Up5, Left7
        -----
        Up: -3
        Down: +3
        Left: -1
        Right: +1
        '''

        '''
        OLD TESTING CODE
        #TO BE DELETED
        #print("start Problem.actions")

        if state == None:
            return

        curr = state.find('_')

        #TO BE DELETED
        #print("current index of _: "+ str(curr))

        if curr<0 or 8<curr:
            print("unknown location of '_', no action available")
            print("make sure '_' is 0-8")
            return

        actionList = []
        #what index has Up action?
        if 2<curr and curr<9:
            #print("Up is allowed")
            actionList.append("D")
        #what index has Down action?
        if -1<curr and curr<6:
            #print("Down is allowed")
            actionList.append("U")
        #what index has Left action?
        if curr != 0 and curr != 3 and curr != 6:
            #print("Left is allowed")
            actionList.append("R")
        #what index has Right action?
        if curr != 2 and curr != 5 and curr != 8:
            #print("Right is allowed")
            actionList.append("L")

        #TO BE DELETED
        #txt="the available actions are {}"
        #print(txt.format(actionList))

        #TO BE DELETED
        #print("end Problem.actions")
        return actionList
        '''

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        #available action and what they do
        '''
        Up: -3
        Down: +3
        Left: -1
        Right: +1
        '''
        '''
        #TO BE DELETED
        #print("start Problem.result")
        #print("initial state: "+state)
        #print("action selected: "+action)

        #if action is not available, return
        if action not in self.actions(state):
            #print("the action is not available: "+action)
            return

        #curr tell the index of '_'
        curr = state.find('_')

        #Up
        if action == "D":
            swapIndex = curr-3
            swap = list(state)
            swap[curr], swap[swapIndex] = swap[swapIndex], swap[curr]
            state=''.join(swap)

        #Down
        elif action == "U":
            swapIndex = curr+3
            swap = list(state)
            swap[curr], swap[swapIndex] = swap[swapIndex], swap[curr]
            state=''.join(swap)
        
        #Left
        elif action == "R":
            swapIndex = curr-1
            swap = list(state)
            swap[curr], swap[swapIndex] = swap[swapIndex], swap[curr]
            state=''.join(swap)

        #Right
        elif action == "L":
            swapIndex = curr+1
            swap = list(state)
            swap[curr], swap[swapIndex] = swap[swapIndex], swap[curr]
            state=''.join(swap)

        #TO BE DELETED    
        #print("Result state: "+state)

        #TO BE DELETED
        #print("end Problem.result")

        return state
        '''

    #goal test should be good
    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        '''
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal
        '''

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        #TO BE DELETED
        #print("start Problem.value")
        #TO BE DELETED
        #print("end Problem.value")

# ______________________________________________________________________________
# Problem Formulation for 8puzzle
class EightPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board, where one of the
    squares is a blank. A state is represented as a tuple of length 9, where  element at
    index i represents the tile number  at index i (0 if it's an empty square) """

    #goal is modified from (1,2,3,4,5,6,7,8,0) to "12345678_"
    #all other code also is modified to take str data type
    def __init__(self, initial, goal="12345678_"):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.find('_')

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        #MODIFICATION
        #the actions is named to fit the requirment of Lab1
        possible_actions = ['D', 'U', 'R', 'L']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('R')
        if index_blank_square < 3:
            possible_actions.remove('D')
        if index_blank_square % 3 == 2:
            possible_actions.remove('L')
        if index_blank_square > 5:
            possible_actions.remove('U')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        #MODIFICATION
        delta = {'D': -3, 'U': 3, 'R': -1, 'L': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return ''.join(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """
        #ignore '_', only look at numbers

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != '_' and state[j] != '_':
                    inversion += 1

        return inversion % 2 == 0 and len(set(state)) == 9
   
# ______________________________________________________________________________
# EightPuzzle with misplaced tile heuristics
class EightPuzzleH1(EightPuzzle):

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """
        return sum(s != g for (s, g) in zip(node.state, self.goal))

# ______________________________________________________________________________
# EightPuzzle with manhattan heuristics
#MODIFICATION
class EightPuzzleH2(EightPuzzle):

    def h(self, node):
        """ Return the heuristic value for a given state."""
        # Manhattan Heuristic Function
        dist = {"1":"012123234", "2":"101212323", "3":"210321432", "4":"123012123", "5":"212101212", 
                "6":"321210321", "7":"234123012", "8":"323212101", "_":"432321210"}   
        heuristic = 0
        for x in node.state:
            goal = dist[x]
            heuristic = heuristic+int(goal[node.state.find(x)])

        return heuristic

# ______________________________________________________________________________
# EightPuzzle with Custom heuristics
# heuristic takes into account the number of direct adjacent tile reversals present
# inspire from http://science.slc.edu/~jmarshall/courses/2005/fall/cs151/lectures/heuristic-search/#:~:text=A%20good%20heuristic%20for%20the%208%2Dpuzzle%20is%20the%20number,direct%20adjacent%20tile%20reversals%20present.
#MODIFICATION
class EightPuzzleH3(EightPuzzle):
    def h(self, node):
        """ Return the heuristic value for a given state."""
        #Custom Function
        #first run exact manhattan 
        dist = {"1":"012123234", "2":"101212323", "3":"210321432", "4":"123012123", "5":"212101212", 
                "6":"321210321", "7":"234123012", "8":"323212101", "_":"432321210"}  
        heuristic = 0
        for x in node.state:
            goal = dist[x]
            heuristic = heuristic+int(goal[node.state.find(x)])
            
        #find direct reversal 
        node.state= node.state.replace("_","9")

        for x in node.state:
            lookForStr = int(node.state.find(x)) +1
            check = int(x) -1
            if int(node.state[check]) == int(x):
                continue
            if int(node.state[check]) == lookForStr:
                heuristic+=1

        node.state= node.state.replace("9","_")

        return heuristic

# ______________________________________________________________________________
# EightPuzzle with Custom heuristics 2
# heuristic takes into account the number of direct adjacent tile reversals present
# using previous heuristic in h3, also taking the number of inverse into consideration.
# for example, if 
'''
8 1 2
3 4 5
6 7 _
'''
# the number of inversion is 7, for (8,1), (8,2), (8,3), ... etc, 
# if a bigger number comes before a smaller number its an inversion
class EightPuzzleH4(EightPuzzle):
    def h(self, node):
        """ Return the heuristic value for a given state."""
        #Custom Function
        #first run exact manhattan 
        dist = {"1":"012123234", "2":"101212323", "3":"210321432", "4":"123012123", "5":"212101212", 
                "6":"321210321", "7":"234123012", "8":"323212101", "_":"432321210"}  
        heuristic = 0
        for x in node.state:
            goal = dist[x]
            heuristic = heuristic+int(goal[node.state.find(x)])
            
        #find direct reversal 
        node.state= node.state.replace("_","9")

        for x in node.state:
            lookForStr = int(node.state.find(x)) +1
            check = int(x) -1
            if int(node.state[check]) == int(x):
                continue
            if int(node.state[check]) == lookForStr:
                heuristic+=1

        node.state= node.state.replace("9","_")

        inversion = 0
        for i in range(len(node.state)):
            for j in range(i + 1, len(node.state)):
                if (node.state[i] > node.state[j]) and node.state[i] != '_' and node.state[j] != '_':
                    inversion += 1
        
        heuristic+=inversion

        return heuristic
        