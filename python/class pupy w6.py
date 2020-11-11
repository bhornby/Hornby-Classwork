#W6 task 1
class Dog():
    def __init__(self, dogName, myColour):
        self.name = dogName
        self.colour = myColour
    
    def bark(self, barkTimes):
        for n in range(barkTimes):
            print('Woof!')
    
    def setColour(self, my_colour):
        self.colour = my_colour
    
    def getColour(self):
        return self.colour
    
    def getName(self):
        return self.name

    def printDogDetails(self):
        print(self.name,self.colour)
    
class Puppy(Dog):
    
    def __init__(self,dogName,myColour):
        super().__init__(dogName, myColour) #this line is the dog constructor everthing after is for the puppy
        self.shoesChewed = 0
    #end procedure
        
    #public procedure chewshoe(myShoesChewed)    
    def chewShoe(self, myShoesChewed):
        self.shoesChewed = self.shoesChewed + myShoesChewed
    #end procedure
      
    def getShoesChewed(self):
        return self.shoesChewed
    #end function

    def bark(self, barkTimes):
        super().bark(1)#do what the parent class did once
        for n in range (barkTimes):
            print(self.name, 'Says Yap!')
            
myDog1 = Dog('James',"light Black")
puppy1 = Puppy("Tim","brown")
puppy2 = Puppy("J", "Black")

'''puppy1.bark(3)
puppy1.chewShoe(3)
print(puppy1.getName(), "has chewed", puppy1.getShoesChewed(), "shoes")'''



print('polymorphis in action')
my_animal_list = [puppy1,myDog1,puppy2]
for animal in my_animal_list:
    animal.bark(3)