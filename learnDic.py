dict1={ 1:"abc",2:"bca",3:"wer",1:"poi",1:"oiu","8":98}
print(type(dict))
print(dict)

mydict=dict(a="parvesh",b="naveen")
print(type(mydict))

mydict1=dict([(6,"par"),(7,"set")])
print(mydict1)

print("ADD ************************************")
dict1[4]="python"
print(dict1)

mydict["c"]="bvf"
print(mydict)

print("Get ************************************")

print(dict1.keys())
print(dict1.values())

print(dict1.get(1))
print(mydict.get("a"))

