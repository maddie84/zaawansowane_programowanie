import Book as bk
import Employee as em
import Library as lb

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
