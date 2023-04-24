class Polygon:
    def __init__(self,no_of_sides):
        self.n=no_of_sides
        self.sides=[0 for i in range(no_of_sides)]
    def input_sides(self):
        self.sides=[float(input('Enter sides'+str(i+1)+':'))for i in range(self.n)]
    def display_side(self):
        for i in range(self.n):
            print('side',i+1,'is',self.sides[i])
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def findArea(self):
        A,B,C=self.sides
        s=(A+B+C)/2
        area=(s*(s-A)*(s-B)*(s-C))*0.5
        print('The area of a triangle is %0.2f'%area)
t=Triangle()
t.input_sides()
t.display_side()
t.findArea()