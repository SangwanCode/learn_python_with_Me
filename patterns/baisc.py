
n=5


# for i in range(n):
#     for j in range(n):
#      print("*",end=" ")
#     print()

## righte angle upward
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()


## righte angle downward
for i in range(n):
    for j in range(i,n):  #(1,5)
        print("*", end=" ")
    print()