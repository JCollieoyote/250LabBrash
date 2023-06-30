class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')

if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()
    
    triangle1_base = float(input())
    triangle1_height = float(input())
    triangle2_base = float(input())
    triangle2_height = float(input())

    triangle1.set_base(triangle1_base)
    triangle1.set_height(triangle1_height)
    triangle2.set_base(triangle2_base)
    triangle2.set_height(triangle2_height)
      
    print('Triangle with smaller area:')  
    
    if triangle1.get_area() < triangle2.get_area():
        triangle1.print_info()
    else:
        triangle2.print_info()