import sys

print(sys.argv[0])

def addition_two_num(x,y):
    c=int(x)+int(y)
    print(c)


addition_two_num(sys.argv[1],sys.argv[2])