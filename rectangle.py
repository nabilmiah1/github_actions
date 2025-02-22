class Rectangle
    def__init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        if self.width <= 0 or self.height <= 0:
            return -1
        else:
            return self.width * self.height
