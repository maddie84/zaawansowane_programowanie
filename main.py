from Classes import Order as ord
from Classes import Book as bk
from Classes import Employee as em
from Classes import Library as lb

# Tworzenie instancji klas
library1 = lb.Library(city="Warszawa", street="Marszalkowska", zip_code="12345",
                   open_hours="9:00 AM - 5:00 PM", phone="111-222-333")
library2 = lb.Library(city="Katowice", street="Ligocka", zip_code="54321",
                   open_hours="10:00 AM - 6:00 PM", phone="444-555-666")

employee1 = em.Employee(first_name="Jan", last_name="Kowalski",
                     hire_date="2022-01-01", birth_date="1990-01-01",
                     city="Warszawa", street="Teatralna", zip_code="12345",
                     phone="987-654-321")

employee2 = em.Employee(first_name="Alicja", last_name="Nowak",
                     hire_date="2022-02-01", birth_date="1985-05-15",
                     city="Tychy", street="Katowicka", zip_code="54321",
                     phone="123-456-789")

book1 = bk.Book(library=library1, publication_date="2022-01-15",
             author_name="Stephen", author_surname="King",
             number_of_pages=200)
book2 = bk.Book(library=library2, publication_date="2022-02-20",
             author_name="Remigiusz", author_surname="Mroz",
             number_of_pages=150)
book3 = bk.Book(library=library1, publication_date="2022-03-25",
             author_name="Harper", author_surname="Lee",
             number_of_pages=180)
book4 = bk.Book(library=library2, publication_date="2022-04-10",
             author_name="Marcin", author_surname="Matczak",
             number_of_pages=220)
book5 = bk.Book(library=library1, publication_date="2022-05-05",
             author_name="Mokito", author_surname="Shinkai",
             number_of_pages=170)

order1 = ord.Order(employee=employee1, student="Halina Sosnowska",
               books=[book1, book2, book3], order_date="2022-03-01")
order2 = ord.Order(employee=employee2, student="Maciej Musial",
               books=[book4, book5], order_date="2022-04-15")

# Wyświetlanie obu zamówień
print(order1)
print(order2)
