class Vector:

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x,self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            res_x = self.x * other.x
            res_y = self.y * other.y
        else:
            res_x = self.x * other
            res_y = self.y * other

        return Vector(res_x, res_y)

    def __eq__(self, other):
        return Vector(self.x == other.x, self.y == other.y)

    def __str__(self):
        return f'Vector = {self.x},{self.y}'


vector_1 = Vector(1, 3)
vector_2 = Vector(1, 2)
vector_3 = vector_1 + vector_2
print(vector_3)
print(vector_1 * 3)
print(vector_1 * vector_2)
print(str(vector_1))
print(vector_1 == vector_2)