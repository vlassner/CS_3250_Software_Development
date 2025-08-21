class Vehicle: 

    def __init__(self, manufacturer, model, year): 
        self.manufacturer = manufacturer 
        self.model = model 
        self.year = year 

    def __str__(self): 
        return f"{self.manufacturer} {self.model} ({self.year})"
    
class Car(Vehicle):

    def __init__(self, manufacturer, model, year, type): 
        super().__init__(manufacturer, model, year)
        self.type = type

    def __str__(self): 
        return f"{super().__str__()} - {self.type}"
    
class Truck(Vehicle):

    DEFAULT_CLASSIFICATION = 1

    def __init__(self, manufacturer, model, year, classification): 
        super().__init__(manufacturer, model, year)
        self.classification = classification if classification > 0 else Truck.DEFAULT_CLASSIFICATION

    def __str__(self): 
        return f"{super().__str__()} - {self.classification}"
    
    
if __name__ == "__main__":
    car = Car("Honda", "Civic Si FG4", 2012, "sedan")
    print(car)
    truck = Truck("Ford", "F350", 2000, 3)
    print(truck)