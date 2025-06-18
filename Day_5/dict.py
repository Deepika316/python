dic={}
print(dic)
dic['name']='Deepu'
dic['roll']=51
dic['pass']=True
print(dic)
print("Accessing the key:",dic['name'])   #adding the element
dic['branch']='CSE'
print(dic)
dic['roll']=75
print("modifeid roll no:",dic)
for i in dic:
    print(f"{i} = {dic[i]}")
print(dic.items())