# n=int(input())
# list=[]
# for i in range(n):
#     dict={}
#     name=input()
#     id=int(input())
#     #dict={"name":name,"id":id}
#     dict["Name"]=name
#     dict["Id"]=id
#     list.append(dict)
# print(list)


n = int(input())
l = []
for i in range(n):
    d = {}
    name = input()
    id = input()
    d["name"] = name
    d["id"] = id
    l.append(d)
print(l)
new_list=[]
search = input()
for i in l:
    if search in i["name"]:
        new_list.append(i)
print(new_list)