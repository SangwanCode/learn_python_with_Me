
# function inside function
def emp_name():
    def emp_skill():
        return "Java"
    return  emp_skill()


def cmp_name():
    return "welcome"

def user_name(x):
    return x

def combine(z,y):
    print(z, y)
    return z+y



print(combine("abc","bca"))

#print(combine(cmp_name(),user_name(" parvesh")))