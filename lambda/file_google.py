
from functools import reduce
# file open and read

google= open("D:\Python_Learning\google_stock_price.csv").readlines()
#print(google)

del google[0]
#print(google)

# convert the elements in float, so that we can find numerical facts

# comperhension approach
gstock= list(map(float,google))
print(gstock)

# regular approach
# gstock=[]
# for x in google:
#     gstock.append(float(x))
# print(gstock)


## Tasks
# largest stock
# smallest Stock
# sum of all stock
# average of all stock


max_value=reduce(lambda x,y: x if x>y else y,gstock)
print(max_value)
min_value=reduce(lambda x,y: x if x<y else y,gstock)
print(min_value)

sum_value=reduce(lambda x,y: x+y,gstock)
print(sum_value)

avg_value=sum_value/len(gstock)
print(avg_value)


#Task :
#1. marks=[('english',50),('math',60),('hindi',45)]
marks=[('english',50),('math',60),('hindi',45),('punjabi',90)]

# total=[]
# def sum_marks(marks):
#     for x in marks:
#         total.append(x[1])
#
# sum_marks(marks)
# print(total)
# print(reduce(lambda x,y:x+y,total))

def sum_marks(x,y):
    if type(x)==int:
        return  x+y[1]
    else:
        return x[1]+y[1]

print(reduce(sum_marks,marks))


# TAsk : excellent stock >400
#           Average stock 200 to 400
#           ok stock  <200


