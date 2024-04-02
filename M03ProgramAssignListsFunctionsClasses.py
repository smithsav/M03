class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)  # Initialize vehicle_type using superclass constructor
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)


def main():
    print("Please enter the details of the vehicle:")
    vehicle_type = input("Car, Truck, Van, SUV: ")  
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sunroof): ")

    # Validate vehicle input
    while vehicle_type not in ['Car', 'Truck', 'Van', 'SUV']:
        print("Invalid input for vehicle type. Please enter Car, Truck, Van, or SUV.")
        vehicle_type = input("Type of vehicle (Car, Truck, Van, SUV): ")

    # Validate doors input
    while doors not in ['2', '4']:
        print("Invalid input for number of doors. Please enter 2 or 4.")
        doors = input("Number of doors (2 or 4): ")

    # Validate roof input
    while roof.lower() not in ['solid', 'sunroof']:
        print("Invalid input for type of roof. Please enter 'solid' or 'sunroof'.")
        roof = input("Type of roof (solid or sunroof): ")

    # Create Automobile object
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Display car information
    print("\nCar Information:")
    car.display_info()


if __name__ == "__main__":
    main()
