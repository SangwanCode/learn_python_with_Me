str="restart"

firstchar=str[0]
print(firstchar)

print(str.replace(firstchar,"$"))
new_str = str.replace(firstchar,"$")


print("*****************************************")
final_str=firstchar+str[1:7]
print(final_str)
final_str1=firstchar+str[1:7]
print(final_str1)
final_str2=firstchar+new_str[1:]
print(final_str2)

print("##########################################")
a="abc, xyz"
b= a.split(",")
print(b[0],b[1])




