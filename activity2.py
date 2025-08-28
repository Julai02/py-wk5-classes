class Vehicle:
    def move(self):
        print("This vehicle moves somehow...")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying through the skies!")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing across the water!")

# Polymorphic behavior
def travel(vehicle):
    vehicle.move()

# Example usage
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    travel(v)
