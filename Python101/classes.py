class Points:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    @staticmethod
    def move():
        print('Move')

    @staticmethod
    def draw():
        print('Draw')


point1 = Points(20, 30)
print(point1.y)