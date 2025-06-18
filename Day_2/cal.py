n1=int(input("Enter the number1:"))
n2=int(input("Enter the numeber2:"))
op=input("Enter the operator:")
operator=["+","-","*","/"]
for i in (operator):
    if op=="+":
        print(n1+n2)
        break
    elif op=="-":
        print(n1-n2)
        break
    elif op=="*":
        print(n1*n2)
        break
    elif op=="/":
        print(n1/n2)
        break
#elif op=="//":
    #print(n1//n2)
else:
    print("Enter valid operator")
