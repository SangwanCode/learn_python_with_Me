# 1 need to find the count of vowels eg parvesh
# 2 need to find vowels and it's counts
'''st = input(" enter the string to find the vowels")

vowels = ["a","e","i","o","u"]
count=0

for x in st:
    if x in vowels:
        count=count+1
print(count)'''

# for 2 requriment paravesh

st = input(" enter the string to find the vowels")
vowels = ["a","e","i","o","u"]
vowDic={}
for x in st:
    if x in vowels:
        vowDic[x]=vowDic.get(x,0)+1

for k,v in vowDic.items():
    print("the vowels",k," is present ",v," times")


# vowDic={}
# count=1
# for x in st:
#     if x in vowels:
#         if x in vowDic.keys():
#             vowDic[x]=vowDic.get(x)+count
#         else:
#             vowDic[x]=count
#
# for k,v in vowDic.items():
#     print("the vowels",k," is present ",v," times")
