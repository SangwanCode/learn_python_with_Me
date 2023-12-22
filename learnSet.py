st={3,4,6,2,8,4,2}
print(type(st))
print(st)

st.add(89)
print(st)
st.add(89)
print(st)
print("###################################")
st1={3,4,5}
st2={'a',6,3}

# st1.update(st2)
# print(st1)

print("All values")

st3=st1.union(st2)
print(st3)
print(st1)
print(st2)

print("Only Duplicate")
st4=st1.intersection(st2)
print(st4)

print("keep all not duplicate")
print(st1)
print(st2)
st1.difference_update(st2)
st1.difference_update(st2)
print(st1)

print("**********************")
print(range(5))



