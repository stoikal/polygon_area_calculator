class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        name = self.__class__.__name__
        return f'{name}(width={self.width}, height={self.height})'

    def get_picture(self):
        width = self.width
        height = self.height
        
        if width > 50 or height > 50:
            return 'Too big for picture.'

        result_str = '' 
        for i in range(height):
            for j in range(width):
                result_str += '*'
            # if i < height - 1:
            result_str += '\n'
        
        return result_str

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_amount_inside(self, rect):
        amount = 0
        if rect.width > self.width or rect.height > self.height:
            return amount
        
        amt_x = self.width // rect.width
        amt_y = self.height // rect.height
        amount = amt_x * amt_y


        return amount

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def __str__(self):
        name = self.__class__.__name__

        return f'{name}(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
