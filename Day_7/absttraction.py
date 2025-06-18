from abc import ABC, abstractmethod
class college(ABC):
        @abstractmethod
        def clg_name(self):
            print("BVC")
class Student(college):
    def clg_name(self):
        print(f"we are in bvcits campus")
x=Student()
x.clg_name() 
 