
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_calculations(self, mass, thickness):
        return round(self._length * self._width * mass * thickness / 1000)


length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
mass = int(input("Enter the mass of asphalt to cover one square meters of the road: "))
thickness = int(input("Enter the thickness: "))

road_to_pave = Road(length, width)
print(road_to_pave.asphalt_calculations(mass, thickness))
