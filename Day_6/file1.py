data=open("Day_6/data.txt","r")
list_data=data.read()
#print(list_data)
list1_data= list_data.split("\n")
#print(list1_data)
dict={}
for i in list1_data:
     print(i)
     split_data= i.split(" ")
     print(split_data)
     dict[split_data[0]]=split_data[1]
print(dict)
     
