import math
class Vector2d:
    def __init__(self, x = 0.0 , y = 0.0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.x)
    
    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.x) 
    
    def leng(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def dot(self, other):
        return 

    




vec1 = Vector2d(5,4)
vec2 = Vector2d(7,8)
vec3 = vec1 + vec2
vec4 = vec1 - vec2 
print(vec3)
print(vec4)
vec5 = Vector2d(4,4)
print(vec5.leng())