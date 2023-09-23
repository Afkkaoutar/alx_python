class Square:
    '''Defining the size of  a square'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    '''Getting the size of  a square'''
    def get_size(self):
        return self.size

    '''Defining a square by size'''
    def set_size(self, size):
        self.size = size

    '''Defining a square by area'''
    def area(self):
        return self.size ** 2

    '''Defining a square by perimeter'''
    def perimeter(self):
        return 4 * self.size
    