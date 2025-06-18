list=[2,3,53,7,9,11,14]
for i in range(0,len(list)):
    x=list[i]
    for j in range(1,len(list)):
        if x < list[j]:
            x=list[j]
print(x)
            
            
        