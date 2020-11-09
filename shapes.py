import turtle

s = turtle.getscreen()
t = turtle.Turtle()


class shape:
    def __init__(self, sides = 0, length = 0) :
        self.sides = sides
        self.length = length


class polygon(shape):
    def info(self):
        print("Polygon is a 2-D shape with straight lines")
        
class square(polygon):
    def show(self):
        for i in range(4):
            t.forward(self.length) #going forward by specified distance
            t.right(90)  #turn by given angle
    

class pentagon(polygon):
    def show(self):
        for i in range(5):
           t.forward(self.length) 
           t.right(72) #exterior angle for a regular pentagon

class hexagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(60)

class octagon(polygon):
    def show(self):
        for i in range(8):
           t.forward(self.length) 
           t.right(45)

class triangle(polygon):
    def show(self):
        t.forward(self.length) 
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)
        
class circle(shape):
    def show(self):
        t.circle(self.length)



shp1 = circle(0,100)
shp1.show()

shp2= square(4,100)
shp2.info()
shp2.show()


