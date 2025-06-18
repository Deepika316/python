class Student:
    def __init__(self,name,id,branch):
        self.x=name
        self.y=id
        self.z=branch
    def display(self):
        print(f"name is {self.x} and my id is{self.y} and my branch is{self.z}")     
clg=Student("Deepu",75,"CSE")
clg1=Student("Bhaskar",51,"CSE")
clg2=Student("SANIKA",45,"CAD")
clg.display()
clg2.display()
clg1.display()


