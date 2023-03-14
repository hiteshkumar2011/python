class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale","Exhale")
        

class Fish(Animal):                    ## To inherith the methods from class Animal 
    
    def __init__(self):
        super().__init__()
    
    def breathe(self):                ## 
        super().breathe()             ## Inheriting the method breath from animal and adding extra functionality
        print("we are swimming underwater")
        
    def swim(self):
        print("We are moving")

f = Fish()
f.swim()  
f.breathe()
print(f.num_eyes)

        
