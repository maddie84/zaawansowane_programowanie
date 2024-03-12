# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
# typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
# parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
# drugim.

def czy_takie_same(lista=[], liczba=0):
    for i in lista:
        if i == liczba:
            return True
        else:
            return False


liczby = [2]
a = 2
liczby2 = [3]
b = 3
print(czy_takie_same(liczby, a))
print(czy_takie_same(liczby2, b))
