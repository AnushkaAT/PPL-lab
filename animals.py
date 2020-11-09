
class Animals:
    def __init__(self, legs=4, eyes=2):
        self.legs = legs
        self.eyes = eyes


class wild_animals(Animals):
    def place(self):
        print("Jungle")

class carnivores(wild_animals):
    def food(self):
        print("Meat")
    
        
class tiger(carnivores):
    def speak(self):
        print("Roar")
    def appearance(self):
        print("Orange white black stripes")
        
class lion(carnivores):
    def speak(self):
        print("Roar")
    def appearance(self):
        print("Mane around face")
        
class hyena(carnivores):
    def speak(self):
        print("laughs like human")
    def appearance(self):
        print("Grey")


                        
class herbivores(wild_animals):
    def food(self):
        print("Plant based")

class deer(herbivores):
    def speak(self):
        print("dummyvalue")
    def appearance(self):
        print("Great horns")
        
class elephant(herbivores):
    def speak(self):
        print("dummyvalue")
    def appearance(self):
        print("Huge and a trunk")
        
class zebra(herbivores):
    def speak(self):
        print("never heared")
    def appearance(self):
        print("Black and white stripes")


        

class domestic_animals(Animals):
    
    def place(self):
        print("Houses of humans")

        
class dog(domestic_animals):
    def speak(self):
        print("bark")
    def youngone(self):
        print("Puppies")
        
class cat(domestic_animals):
    def speak(self):
        print("meow")
    def youngone(self):
        print("Kitten")
        
class cow(domestic_animals):
    def speak(self):
        print("moo")
    def youngone(self):
        print("Calf")
        
class goat(domestic_animals):
    def speak(self):
        print("dummyvalue")
    def youngone(self):
        print("Calf")

p1=Animals(4, 3)
coco= cow()
coco.speak()
coco.place()
coco.youngone()
print(p1.eyes)
print(p1.legs)



