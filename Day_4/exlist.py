x=int(input("Enter number:"))
l=[2,3,4,7,9,11,14]
val_flag=False
for y in  range(0,len(l)):
    if l[y]==x:
        val_flag=True
        break
if val_flag:
    print("found")
else:
    print("not found")
        