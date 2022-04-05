# Modeling Real Concepts

#define a class capital letter first
class Point:
    #define Constructors
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("move")
    

    def draw(self):
        print("draw")

    
point = Point(10,20)
print(point.x)
point.draw()
point.move()



