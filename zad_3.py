class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.area} sqm, {self.rooms} rooms, {self.price}$, {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)      #dziedziczy z konstruktora z klasy Property
        self.plot = plot

    def __str__(self):
        return f"House: {super().__str__()}, Plot size: {self.plot} sqm"

class Flat(Property):
    def __init__(self,area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {super().__str__()}, floor: {self.floor}"
    
# Tworzenie obiektów klasy House i Flat
house = House(area=150, rooms=5, price=300000, address="123 Main Street", plot=500)
flat = Flat(area=80, rooms=3, price=150000, address="456 Side Street", floor=2)

# Wyświetlanie obiektów
print(house)
print(flat)