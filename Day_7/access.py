class animal:
    name="Deepu"   #default parameter
    def __init__(self,name,number):
        self.a=name
        self.b=number
    def change_name(self,new_name,new_num):
        self.a=new_name
        self.b=new_num
    def __str__(self):   # we are accessing the object directly by using str function
        return f"object name is {self.a}"
    def display(self):
        print(f"{self.a},{self.b}")
x=animal("sanika",324234)
x.change_name("Bvc",43253)
x.display()
print(x.name)  #callimg default parameter
print(x)

    
