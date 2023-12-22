

def abc():
    print("hi")

def abc_para(fistname,lastname="notmentioned"):
    print("welcome", fistname,lastname)



#abc()

def add_num(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)
    return sum

add_num(3,5,6,7,8,9,10,name="parves",lastname="kumar",email="abc.com")
