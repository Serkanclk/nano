class Rectangle:
    def __init__(self,c,w,l):
        self.width = w
        self.length = l
        self.color = c
    def area(self):
        self.area = self.width*self.length
        return self.area
    def per(self):
        self.perimeter = 2*self.width+2*self.length
        return self.perimeter

c1 = 'red'
w1 = 3
l1 = 4
rect1 = Rectangle(c1,w1,l1)
areaR1 = rect1.area()
print(areaR1)

c2 = 'blue'
w2 = 3
l2 = 5
rect2 = Rectangle(c2,w2,l2)
areaR2 = rect2.area()
print(areaR2)
