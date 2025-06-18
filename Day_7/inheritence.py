# class Animal:
#     sound="Bow Bow"
#     def sound_fun(self):
#         print(f"The sound of the dog is {self.sound}")

# class Dog(Animal):
#     def color(self):
#         print("Dog")
# oobject=Dog()
# print(oobject.sound)
# oobject.sound_fun()
# oobject.color()




# HIERARCHIAL
# class Animal:
#      sound="Bow Bow"
#      def sound_fun(self):
#         print(f"The sound of the animal is {self.sound}")

# class cat(Animal):
#     sounds="Meow Meow"


# class Dog(Animal):
#     def color(self):
#         print("Dog")

# oobject2=cat()
# print(oobject2.sounds)
# oobject2.sound_fun()
# print(oobject2.sound)


# oobject1=Dog()
# print(oobject1.sound)
# oobject1.sound_fun()
# oobject1.color()
  


#MULTIPLE
# class Dog():
#     def color(self):
#         print("Dog")
# class cat():
#     sounds="Meow Meow"
# class Animal(Dog,cat):
#     pass
# x=Animal()
# x.color()
# print(x.sounds)

#MULTILEVEL
# class Animal():
#     legs=4
#     #print("eawesdf")
# class cow(Animal):
#     #print("jghl")
#     color="White"
# class calf(cow):
#     pass
# x=calf()
# print(x.legs)
# print(x.color)


#HYBRID
class Animal:
    sound="Bow Bow"
    def sound_fun(self):
        print(f"The sound of the dog is {self.sound}")

class Dog(Animal):
    def color(self):
        print("Dog")
class Cat:
    a="hai"
class Child(Cat,Dog):
    b="we are animals"
x=Child()
print(x.b)
print(x.a)
x.color()
x.sound_fun()






