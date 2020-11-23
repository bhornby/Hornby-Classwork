class Dog():
    def __init__(self, my_name):
        self.name = my_name
        self.colour = ''
    #end procedure
        
    def set_colour(self, my_colour):
        if my_colour in ("Black","Brown","Golden"):
            self.colour = my_colour
    
    def get_colour(self):
        return self.colour
    #end function

class Puppy(Dog):
    def __inint__(self):
        self.shoesChewed = 0
        self.name =''
    
    def get_name(self, my_name):
        return self.name

    def set_name(self, my_name):
        self.name = my_name
        
    def set_chew_shoe(self,numshoes):
        self.shoesChewed = self.shoesChewed + numshoes
    
    def getshoeschewed():
        return shoesChewed

new_puppy = Puppy
new_puppy.name = 'James'
new_puppy.set_chew_shoe(new_puppy.name,10)

print(new_puppy.getshoeschewed())
