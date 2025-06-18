import cont_fun as ctf
contacts = {}

#("Day_6/cont_data.txt","w")
#print(file)

print("\tContacts App")

while True:
    try:
        print("\nChoices :")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Delete contact")
        print("4. Find contact")
        print("5. Edit contact")
        print("6. Exit")
        choice = int(input("Enter choice : "))

        if choice == 1:
            ctf.add_contact(contacts)
        elif choice == 2:
            ctf.view_contacts(contacts)
        elif choice == 3:
            ctf.delete_contact(contacts)
        elif choice == 4:
            ctf.find_contact(contacts)
        elif choice == 5:
            ctf.edit_contact(contacts)
        else:
            print("End")
            break
    except Exception as error:
        print(f" Error is {error}")
    finally:
        print("The Contact is saved")