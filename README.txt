Author: Yee Chuen Teoh
Title: COM S 572 Lab 1

How to run 8puz.py

Instruction:
- add 8puz.py, Pformulation.py, search.py, and utils.py are placed in the same folder (example 'Lab1')
- Open terminal, first change the dist by typing in 'C:' (could be 'E:' if you file is in E: disk)
- then change directory to the folder directory
    > to do this, type 'cd C:\filename\filename\Lab1' (filename indicate folder name before Lab1 and before that)
- now that you are in the right directory
- type the following to run 8puz.py
    > 'python 8puz.py --fPath <filename> --alg <algorithm>
    > replace <filename> with the file you want to run
    > replace <algorithm> with the algorithm of your choice
    > more detail on --fPath and --alg below
- the terminal will run the algorithm on the file and show the result

Notes:
--fPath
    > you can choose to input either a .txt file OR any folder in the same directory
    > if input .txt file
        > 8puz.py will run the selected algorithm on that single file
    > if input folder (example 'Part2')
        > 8puz.py will run all the .txt file in that folder
    > be sure that all the .txt file are in the format of:
        x x x
        x x x
        x x x       
    > x represent any number from 1 - 8 and a '_' to represent blank space
    > only use each number and '_' once
    > the .txt file will serve as the starting state of the 8 puzzle
    
--alg
    > here you have 6 options (BFS / IDS / h1 / h2 / h3 / h4 / all)
    > the picking the default options will show only details of the search algorithm 
    > Or you can add '*' to the options to show only the average result (example --alg BFS*)
    > Or you can add '**' to the options to show both details and average result (example --alg BFS**)
    > "BFS" runs Breadth First Graph Search 
    > "IDS" runs Iterative Deepening Search
    > "h1" runs Astar Search using misplaced tiles as heuristic
    > "h2" runs Astar Search using manhattan distance as heuristic
    > "h3" runs Astar Search using manhattan distance and reversal as heuristic
        > reversal is when two number are in a location reverse of their goal space location
        > for example
            1 2 3
            7 5 6
            4 8 _
        > here there is a pair of reversal 7 and 4 
        > add 2 to the heuristic for each pair of reversal
    > "h4" runs Astar Search using h3's heuristic with addition of inversion
        > inversion is when a larger number appears before a smaller, hence inverse
        > for example
            8 2 3
            4 5 6
            7 1 _
        > there is 7 inversion, (8,2)(8,3)(8,4)(8,5)(8,6)(8,7)(8,1)
    > "all" runs all 6 search algorithm on the selected .txt file