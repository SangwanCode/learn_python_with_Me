name="Parvesh"
print(type(name))
print("length of the name "+ str(len(name)))
print(name[0])
print(name[-2])

print(name[0:3])
print(name[0:])
print(name[:6])
print("******************************************")
#(start:end: step)
print(name[0:len(name):3])
print("################################################")
name1='   parvesh kumar    '
#print(name1[::-1])
print(name1.strip())
print(name1.lstrip())
print(name1.rstrip())

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

emp="parvesh/work/in/abc"
lst=emp.split("/",1)
print(lst)

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

empname="parvesh"
print(empname.capitalize())

empname="Parvesh"
print(len(empname))
print(empname.center(10,"#"))







