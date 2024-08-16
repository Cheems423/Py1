class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        dt=self.width*self.length
        return dt
    
    def perimeter(self):
        cv=(self.width+self.length)*2
        return cv
    
    def display(self):
        print(f'Chiều rộng: {self.width}, Chiều dài: {self.length}, Chu vi: {self.perimeter()}, Diện tích: {self.area()}')