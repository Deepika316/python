import opr 
#import opr as deepu----rename the module
#from opr import add---importing particular function
n1=int(input("Enter number: "))
while True:
    op=input("Enter operater: ")
    if op=="=":
        break

    n2=int(input("Enter number: "))
    if op=="+":
        n1=opr.add(n1,n2)
    elif op=="-":
        n1=opr.sub(n1,n2)
    elif op=="/":
        n1=opr.div(n1,n2)
    elif op=="*":
        n1=opr.mul(n1,n2)
    elif op=="%":
        n1=opr.mod(n1,n2)
    elif op=="**":
        n1=opr.pow(n1,n2)
    print(n1)
print("Final value:",n1)

