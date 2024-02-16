class Point:

    def __init__(self, x=0.0, y=0.0):
        self.__setter_x(x)
        self.__setter_y(y)

    def __setter_x(self,x):
        if isinstance(x,(int,float)):
            self.__x = x
        else:
            raise ValueError('Значением может быть только число')

    def __setter_y(self,y):
        try:
            if isinstance(y,(int,float)):
                self.__y = y
            else:
                raise ValueError('Значением может быть только число')
        except ValueError:
            print('')
    def get_data(self):
        return self.__x,self.__y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

point_0 = Point(12,2)
print(point_0.get_data())
point_1 = Point(1,2)
print(point_1.get_x())
print(point_1.get_y())
