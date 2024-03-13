class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
        self.books = []

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}, " \
               f"{self.open_hours}, {self.phone}"
