class Square: 

    # faulty constructor on purpose
    def __init__(self, side: int) -> None:
        if side <= 0:
            self.side = 1
        else:
            self.side = int(side)

    def area(self): 
        return self.side * self.side 
    
    # faulty method on purpose
    def perimeter(self): 
        return self.side * 4
