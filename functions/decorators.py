

# existing function need to have some additional functionaltiy
# we can change the behaviour at the complie time

# syntax : def decorator_function(function_name) :   return the function.


def num():
    return 5


def decoratorfun(func):
    def inner_fun():
        return num()*2
    return inner_fun

# multiple_num=decoratorfun(num)
# print(multiple_num())

# functionname ------return the whole function
# function()----- call the function


def div_num(a,b):
    return a/b

def dec_num(func):
    def inner_fun(a,b):
        if a < b:
            a, b = b, a
        print("value of numerator", a)
        print("value of denominator", b)
        return div_num(a,b)
    return inner_fun

# result_div_num=dec_num(div_num)
# print(result_div_num(2,6))

########## create funtion greet new users
#  welcome username

# user=Parvesh ---- welcome parvesh
