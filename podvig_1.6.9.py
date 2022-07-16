

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self) -> object:
        return Point(self.x, self.y)

pt = Point(1, 2)
pt_clone = pt.clone()
print(pt_clone.x)