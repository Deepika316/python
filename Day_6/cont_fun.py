def add_contact(contacts):
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile
    file=open("Day_6/cont_data.txt","a")
    file.write(f"{name} {mobile}\n")
    file.close()
def view_contacts(contacts):
    file=open("Day_6/cont_data.txt","r")
    if  file:
        file1=file.readlines()
        for j in file1:
            print(j.strip("\n"))
            file.close()
    else:
        print("There is no such type of contact")
    
def delete_contact(contacts):
    file=open("Day_6/cont_data.txt","r")
    name_to_delete = input("Enter contact name to delete :")
    
    del contacts[name_to_delete]
    print("deleted contact " , name_to_delete)

def find_contact(contacts):
    query = input("Enter name to search : ").lower()
    found = False
    file=open("Day_6/cont_data.txt","r")
    file2=file.readlines()
    for key in file2:
        if query in key.lower():
            print(key)
            found = True
    if not found:
         print("contact not Found")
    file.close()

def edit_contact(contacts):
    file=open("Day_6/cont_data.txt","r")
    file3=file.readlines()
    name_to_edit = input("Enter contact name to edit :")
    number = int(input("Enter new number: "))
    contacts[name_to_edit] = number
    print("Edited contact : " , name_to_edit)