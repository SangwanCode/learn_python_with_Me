
'''
    1=
    1*2=
    1*2*3=
    1*2*3*4=
'''
z=1
n = 5

for x in range(1,n+1):
    z*=x
    for y in range(1,x+1):
        # print(y,"*",end="")
        if y==x:
            print(y,end="")
        else:
            print(y,end="*")
    print("=",z)




