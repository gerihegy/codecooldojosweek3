import sys
import fileinput

with open("ideas.txt","a") as x:
    print("What's your latest idea?")
    newIdea=input()
    x.write(newIdea+"\n")
    x.close()


