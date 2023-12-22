

#snytax : filter( bool_function, data)

data=[1,2,3,4,5,6,7]

print(list(filter( lambda num: num%2==0,data )))

item=[10,10.3,True,'parvesh',20]

print(list(filter( lambda n: type(n)==int,item  )))

moviechar=['dc-spiderman','dc-ironman','marvel-wonderwomen','marvel-hulk']

print(list(filter( lambda c:c.startswith('dc') ,moviechar)))

