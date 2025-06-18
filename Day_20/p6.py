def slug_generator(x):
    x=x.lower()
    x=list(x)
    result=""
    for i in range(0,len(x)):
        if x[i].isalnum():
            result+=x[i]
        elif x[i]==" ":
            result+='-'
        else:
            continue
    return result
title=input()
print(slug_generator(title))

