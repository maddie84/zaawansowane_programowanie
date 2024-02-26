# Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5
# dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
# zwróci. Zadanie należy wykonać w 2 wersjach:
# 1. Wykorzystując pętle for .
# 2. Wykorzystując listę składaną.

def mnozenie_liczb(liczby):
    for liczba in liczby:
        print(liczba*2)

liczby_lista = [1,2,3,4,5]
mnozenie_liczb(liczby_lista)


def mnozenie(liczby):
    wynik = [liczba * 2 for liczba in liczby]
    return wynik

liczby_lista = [1,2,3,4,5]
print(mnozenie(liczby_lista))