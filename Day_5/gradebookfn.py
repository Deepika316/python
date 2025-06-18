def add_student(gradebook):
    name=input("Enter the student name:")
    marks=list(map(int,input("Enter the student marks:").split(",")))
    gradebook[name]=marks

def view_student(gradebook):
    for i,j in gradebook.items():
        print(f"{i} : Marks{j} average =",sum(j)/len(j))
def find_student(gradebook):
    name=input("Enter name:")
    #for name in gradebook:
    print(f"{name}  {gradebook[name]}")

def update_student(gradebook):
   name=input("Enter name:")
   if name in gradebook:
    new_marks=list(map(int,input("Enter new marks:").split(",")))
    gradebook[name]=new_marks
   else:
        print("Name not found")

      
def remove_student(gradebook):
    another_name=input("Enter name:")
    del gradebook[another_name]