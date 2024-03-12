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


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, " \
               f"{self.hire_date}, {self.birth_date}, " \
               f"{self.city}, {self.street}, {self.zip_code}, {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.library.books.append(self)
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}, " \
               f"{self.publication_date}, {self.number_of_pages} pages"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_descriptions = [str(book) for book in self.books]
        return f"Order: {self.employee.first_name}, " \
               f"{self.employee.last_name}, {self.student}, " \
               f"{', '.join(book_descriptions)}, {self.order_date}"


# Tworzenie instancji klas
library1 = Library(city="Warszawa", street="Marszalkowska", zip_code="12345",
                   open_hours="9:00 AM - 5:00 PM", phone="111-222-333")
library2 = Library(city="Katowice", street="Ligocka", zip_code="54321",
                   open_hours="10:00 AM - 6:00 PM", phone="444-555-666")

employee1 = Employee(first_name="Jan", last_name="Kowalski",
                     hire_date="2022-01-01", birth_date="1990-01-01",
                     city="Warszawa", street="Teatralna", zip_code="12345",
                     phone="987-654-321")

employee2 = Employee(first_name="Alicja", last_name="Nowak",
                     hire_date="2022-02-01", birth_date="1985-05-15",
                     city="Tychy", street="Katowicka", zip_code="54321",
                     phone="123-456-789")

book1 = Book(library=library1, publication_date="2022-01-15",
             author_name="Stephen", author_surname="King",
             number_of_pages=200)
book2 = Book(library=library2, publication_date="2022-02-20",
             author_name="Remigiusz", author_surname="Mroz",
             number_of_pages=150)
book3 = Book(library=library1, publication_date="2022-03-25",
             author_name="Harper", author_surname="Lee",
             number_of_pages=180)
book4 = Book(library=library2, publication_date="2022-04-10",
             author_name="Marcin", author_surname="Matczak",
             number_of_pages=220)
book5 = Book(library=library1, publication_date="2022-05-05",
             author_name="Mokito", author_surname="Shinkai",
             number_of_pages=170)

order1 = Order(employee=employee1, student="Halina Sosnowska",
               books=[book1, book2, book3], order_date="2022-03-01")
order2 = Order(employee=employee2, student="Maciej Musial",
               books=[book4, book5], order_date="2022-04-15")

# Wyświetlanie obu zamówień
print(order1)
print(order2)
