class Table:
    count = list()
    def __init__(self,x,y):
        self.count.append([x,y])

class Point:

    def __init__(self, x: float=0.0, y: float=0.0):
        self.x = x
        self.y = y
        Table(x,y)

    def print_point(self):
            print('Точка в координате {}x{}\nКоличество точек: {}\nТочки{}'.format(
                self.x,
                self.y,
                len(Table.count),
                Table.count
        ))
point_0 = Point()
point_1 = Point(10.6,1.3)
point_1.print_point()
point_2 = Point(5,2)
point_2.print_point()
point_3 = Point(12,3)
point_3.print_point()