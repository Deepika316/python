# mail=input()
# # print(mail)
# print(mail[1:len(mail)-1])
# if '@' in mail and '.' in mail:
#     print("entered mail is valid")
# else:
#     print("Entered mail is invalid")

def valid_email(mail):
    list=['`','!','#','$','%','^','*','(',')',',',':',';','{','}','[',']',';']
    for i in list:
        return False
    if '@' in mail and '.' in mail:
        return True
    else:
        return False
    
mail=input()
print(valid_email(mail))


