vehicle_type = input("Input vehicle type: ")
year = input("Input year: ")
make = input("Input make: ")
model = input("Input model: ")
doors = input("Input number of doors (Must be 2 or 4): ")
roof = input("Input type of roof (Must be either solid or sun roof): ")
class Vehicle:
    def __init__(self, vehicle_type):
          self.vehicle_type = vehicle_type
class Automobile(Vehicle):
     def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
my_car = Automobile(vehicle_type, year, make, model, doors, roof)
print(f"""
      Vehicle Type: {my_car.vehicle_type}
      Year: {my_car.year}
      Make: {my_car.make}
      Model: {my_car.model}
      Number Of Doors: {my_car.doors}
      Type Of Roof: {my_car.roof}
""")