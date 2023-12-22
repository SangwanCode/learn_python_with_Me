emp=[100,23,56,23]
emp1=[4,3,6]
print(emp)
print(emp1)

print("********************")
# emp.extend(emp1)
# print(emp)
# print(emp1)

# emp3=emp+emp1
# print(emp3)
# print(emp)
# print(emp1)

#emp.sort(reverse=True)
emp.reverse()
print(emp.count(23))
print(emp)

emp3=emp.copy()
print(emp3)