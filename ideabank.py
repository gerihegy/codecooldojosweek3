import sys
import fileinput



def to_do_app():
    with open("ideas.txt","a") as f:
        print("What's your latest idea?")
        newIdea=input()
        f.write(newIdea+"\n")

def read_file():
    with open("ideas.txt","r") as f:
       return f.readlines()



def list_to_do():
    idea_list= read_file()
    index= 1
    for line in idea_list:
        print(f" {index},{line[:-1]}")
        index +=1

def is_int(input):
    return str(input).isnumeric()


def rewrite_idea_file():
    with open("ideas.txt","w") as f:
        f.writelines(to_dos)


if len(sys.argv) == 3 and sys.argv[1] == "--delete" and is_int(sys.argv[2]):
    to_dos = list(read_file())
    idea_to_delete = int(sys.argv[2])
    del to_dos[idea_to_delete]
    rewrite_idea_file()
else:
    to_do_app()


list_to_do()








