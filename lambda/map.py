

# snytax : map ( function , data)

# def squar_num(num):
#     return  num*num
#
# newlist=[]
data=[1,2,3,4,5,6]
# for x in data:
#     y=squar_num(x)
#     newlist.append(y)
#
# print(newlist)

# print(list(map( lambda num: num*num,data)))
#
# print(set(map( lambda num: num*num,data)))
# print(tuple(map( lambda num: num*num,data)))
#
# print(dict(map( lambda num:(num,num*num) ,data)))

color=['red','orange','blue','indigo']


def find_len(x):
    return len(x)

#print(list(map(len,color)))

print(list(map(find_len,color)))

print([ len(c) for c in color ])

# lst1=[12.3,3.4,5.6]
#
# print(list(map(int,lst1)))





