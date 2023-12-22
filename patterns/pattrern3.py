

n=5


for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):  #down
        print("*", end=" ")

    for j in range(i+1,n):  #down
        print("*", end=" ")
    for j in range(i+1):
        print(" ", end=" ")
    print()

for i in range(n):
    for j in range(i,n):  #(1,5)
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")

    for j in range(i):
        print("*", end=" ")
    for j in range(i,n):  #(1,5)
        print(" ", end=" ")
    print()