# Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną
# metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
# ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy
# stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
# zwracała true , a dla drugiego false .

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        srednia = sum(self.marks) / len(self.marks)
        if srednia > 50:
            return True
        else:
            return False
        
stud1 = Student("Hubi", [5, 10, 40])
stud2 = Student("Magda", [80, 80, 40])

print(stud1.is_passed())
print(stud2.is_passed())