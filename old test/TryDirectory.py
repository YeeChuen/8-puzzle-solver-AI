#Author: Yee Chuen Teoh
#Title: test file for learning reading files

# make sure terminal in 
# D:\Coding Software\GradProjectVSC\COMS_572_Lab1
# import os to check 
import os
import argparse
import glob

''' OLD TEST
file = open("COMS_572_Lab1/S1.txt", "r")
readfile = file.read()
print(os.getcwd())
print(readfile)
'''

'''new test, read file using terminal'''
#create new parse
parser = argparse.ArgumentParser()
#add argument to parse
parser.add_argument('--file', type=str, required=True)
#take argument
args = parser.parse_args()

def readfile(content):
    file = open(content, "r")
    print(file)
    print(file.read())

#must be txt file
if args.file.endswith('.txt'):
    readfile(args.file)
else:
    folder=args.file
    folder = folder+"/*.txt"
    txt_files=glob.glob(folder)
    for x in txt_files:
        readfile(x)


'''new test, read a files in a folder
#uses glob module
#/*.txt takes every 
txt_files = glob.glob("Part2/*.txt")
print(txt_files)
for x in txt_files:
    readfile(x)
'''
