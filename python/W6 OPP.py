class Dog():# a blue print that defines its methods and attributes and an object is an instance of a class and the constructor is a method that is called automatically when a new object is created instanciation takes a class which is a  blueprint and calls a constructor
    
    def __init__(self, my_name):
        self.name = my_name
        self.colour = ''
    #end procedure
        
    def set_colour(self, my_colour):
        if my_colour in ("Black","Brown","Golden"):
            self.colour = my_colour
        #end if 
    #end procedure
    #when setting the colour you can only set the colour to the passed arguments
    
    def get_colour(self):
        return self.colour
    #end function
        
my_Dog1 = Dog('James') 
my_Dog2 = Dog('Fido')


#my_Dog1.name = 'James'
#my_Dog2.name = 'Fido'

my_Dog1.set_colour ('Golden')
my_Dog2.set_colour ('Brown')
#need brackets as using a function rather than assigning a varible

print(my_Dog1.name)
print(my_Dog1.get_colour())

print(my_Dog2.name)
print(my_Dog2.get_colour())
#as its now a function need to use brackets at the end

#two underscores each side of the __init__
        # no need for getter or setter methods as all are public
        #self is like a hidden parameter
#so when created we specify the new when creating the new dog
#always give the created object a name to give a colour when created need to pass parameters
   






