import gradebookfn as gd
gradebook={}

print("---GRADE BOOK---")
while True:
    choice = int(input("Enter choice : "))
    print("1.Add Student")
    print("2.view all student details")
    print("3.Find the student")
    print("4.update the student")
    print("5.remove student")
    print("6.Exit")

    if choice==1:
        gd.add_student(gradebook)
    elif choice==2:
        gd.view_student(gradebook)
    elif choice==3:
        gd.find_student(gradebook)
    elif choice==4:
        gd.update_student(gradebook)
    elif choice==5:
        gd.remove_student(gradebook)
    else:
        break


        




