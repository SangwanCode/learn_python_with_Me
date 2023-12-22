


# def num1(x):
#     return x*x
# num1(3)

# lambda ---- 1 liner function with no name
# syntax  lambda <input variable>: <output expression>

getsqr= lambda  num: num*num

print(getsqr(6))

data= [1,2,2,3,4,4,5,6,5]

unqi= lambda  data: set(data)

print(unqi(data))

oddEven= lambda  data: "even" if data%2==0 else "Odd"

print(oddEven(8))

add_two= lambda x,y: x+y
print(add_two(5,8))