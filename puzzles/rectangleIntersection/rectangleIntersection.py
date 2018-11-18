class Rectangle:
    def __init__(self, dimensions):
        self.x = dimensions['x']
        self.y = dimensions['y']
        self.w = dimensions['w']
        self.h = dimensions['h']

def findIntersection(r1: Rectangle, r2: Rectangle):
    def isIndersected(r1, r2):
        return (r1.x + r1.w >= r2.x and r2.x + r2.w >= r1.x and
            r1.y + r1.h >= r2.y and r2.y + r2.h >= r1.y)

    if not isIndersected(r1, r2):
        return False

    return Rectangle(
        {
            'x': max(r1.x, r2.x),
            'y': max(r1.y, r2.y),
            'w': min(r1.x + r1.w, r2.x + r2.w) - max(r1.x, r2.x),
            'h': min(r1.y + r1.h, r2.y + r2.h) - max(r1.y, r2.y)
        }
    )

if __name__ == '__main__':
    intersection = findIntersection(
        Rectangle({'x':1, 'y':1, 'w':10, 'h':10}),
        Rectangle({'x':2, 'y':2, 'w':10, 'h':10})
    )
    print(intersection.x, intersection.y, intersection.w, intersection.h)
