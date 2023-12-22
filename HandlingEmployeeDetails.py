# user input how many emp u want to add
# user enter name
#enter employee skills
# which emp skills you want to see


empCount=int(input("enter how many emp you want to add "))
empRecord={}

for x in range(1,empCount+1):
    empName= input("enter the emp name ")
    empSkills = input("enter the emp skills")
    empRecord[empName]=empSkills
    print("emp record successfully added")

# empSearch=input("Please enter the emp name you want to get the skills ")

# for y in empRecord.keys():
#     if y==empSearch:
#         print("the skills of the emp are : ",empRecord[y])
#         break
while True:
    empSearch = input("Please enter the emp name you want to get the skills ")
    if empSearch in empRecord.keys():
        print("The skills of the emp are ;" + empRecord[empSearch])
    else:
        print("no recored found")

    newSearch=input(" do you want to search again . write Y or N")
    if newSearch == "N":
        break


