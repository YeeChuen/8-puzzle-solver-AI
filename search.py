#Author: Yee Chuen Teoh
#Title: COM S 572 Lab 1
#Reference: Search (Chapters 3-4) textbook Artificial Intelligence_ A Modern Approach

from ast import Str
import sys
from collections import deque
from time import time
import time

from utils import *

# ______________________________________________________________________________
# NODE

class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    #nodeNume is modification to keeptrack generated node
    def __init__(self, state, parent=None, action=None, path_cost=0, nodeNum=1):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
        self.nodeNum=nodeNum

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def updateNodeNum(self, nodeNum):
        self.nodeNum = nodeNum

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # We want for a queue of nodes in breadth_first_graph_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        # We use the hash value of the state
        # stored in the node instead of the node
        # object itself to quickly search a node
        # with the same state in a Hash Table
        return hash(self.state)


# ______________________________________________________________________________
# BFS (Breadth First Graph Search)
#MODIFIED time
def breadth_first_graph_search(problem, starttime, mintime):
    """[Figure 3.11]
    Note that this function can be implemented in a
    single line as below:
    return graph_search(problem, FIFOQueue())
    """

    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        #MODIFIED time
        currtime = time.time()
        if currtime - starttime >= mintime:
            return Node("Timed out.")

        node = frontier.popleft()
        explored.add(node.state)
        
        childList=node.expand(problem)
        for child in childList:
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    child.updateNodeNum(len(explored)+len(frontier)+1)
                    return child
                frontier.append(child)
    return None

# ______________________________________________________________________________
# IDS (Iterative Deepening Search)

def iterative_deepening_search(problem, starttime, mintime):
    """[Figure 3.18]"""
    #totalnode keep track of total number of generated node
    #in each depth
    totalnode=0

    for depth in range(0,50):
        result = depth_limited_search(problem, starttime,totalnode,mintime, depth)
        if result.state != 'cutoff':
            #print("depth: "+str(depth)+ ", node at depth: "+ str(result.nodeNum)+", totalnode: "+str(result.nodeNum+totalnode))
            result.nodeNum+=totalnode
            return result
        #right here, the total node during any depth search is return 
        #with a node containing the total node in node.nodeNum
        #and the state 'cutoff' to indicate it is cutted off with n amount of node generated
        totalnode += result.nodeNum
        #print("depth: "+str(depth)+ ", node at depth: "+ str(result.nodeNum)+", totalnode: "+str(totalnode))
    
    #MODIFIED below checks if cutoff work properly
    if result.state == 'cutoff':
        '''below prints the cutoff'''
        #print("depth reaches cutoff limit")
        #print("depth is "+str(depth))
        return None
            

def depth_limited_search(problem, starttime,totalnode,mintime, limit=50):
    """[Figure 3.17]"""
    #TRY2 using list
    nodelist = []

    def recursive_dls(node, problem, limit, starttime, totalnode,mintime):
        #MODIFIED time
        currtime = time.time()
        #TRY2 does not removes duplicate, 
        #which is good as same node can appear in different path, 
        #as long as its not cycle
        nodelist.append(node)

        if currtime - starttime >= mintime:
            return Node("Timed out.")

        if problem.goal_test(node.state):
            #MODIFIED
            node.updateNodeNum(len(nodelist))
            return node

        elif limit == 0:
            #MODIFIED, change cutoff to Node with state cutoff
            cutoff = Node('cutoff')
            cutoff.updateNodeNum(len(nodelist))
            return cutoff
        else:
            cutoff_occurred = False
            for child in node.expand(problem):

                #TRY2 WORK
                ancestor = child.path()
                ancestor.remove(child)

                if child in ancestor:
                    continue

                result = recursive_dls(child, problem, limit - 1, starttime, totalnode,mintime)
                
                #MODIFIED add a new constrain, is not None
                if result is not None and result.state == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return result if cutoff_occurred else None

    # Body of depth_limited_search:
    #MODIFIED
    return recursive_dls(Node(problem.initial), problem, limit, starttime, totalnode,mintime)

# ______________________________________________________________________________
# A*
def astar_search(problem, starttime,mintime, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, starttime, mintime, lambda n: n.path_cost + h(n), display)

def best_first_graph_search(problem, starttime,mintime, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        #MODIFIED time
        currtime = time.time()
        if currtime - starttime >= mintime:
            return Node("Timed out.")

        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")

            node.updateNodeNum(len(explored)+len(frontier)+1)
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None