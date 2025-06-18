n=int(input("Enter number:" ))
pr_flag =True
for i in range(2,int(n/2)+1):
    if n%i==0:
        pr_flag=False
        break
if pr_flag:
    print("It is a prime")
else:
    print("It is not a prime")
            