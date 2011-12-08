import math
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distanceTo(self,p):
        return math.sqrt(pow(self.x-p.x,2) + pow(self.y-p.y,2))
    def prints(self):
        print "(" + str(self.x) + "," + str(self.y) + ")"
    
d = Point(2,2)
a = Point (3,3)
print d.distanceTo(a)
