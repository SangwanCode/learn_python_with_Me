

# is a special function that is used for data aggregation.
# funtools lib
# return the value of x

# reduce(function, data)

from functools import  reduce

sum_val=reduce( lambda x,y : x*y,[1,2,3,4,5,6])
print(sum_val)



