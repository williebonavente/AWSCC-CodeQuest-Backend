"""Author: Willie M. Bonavente
    Date: 12/02/2023
"""

class Rectangle:
    
    def __init__(self, length, width):
        
        self.length = length
        self.width = width
    
    # Methods
    def area(self):
        area = self.length * self.width
        return f"Area: {area}"
    
    def perimeter(self):
        perimeter = 2*(self.length + self.width)
        return f"Perimeter: {perimeter}"
    

rectangle_1 = Rectangle(25, 25)
print(rectangle_1.area())
print(rectangle_1.perimeter())