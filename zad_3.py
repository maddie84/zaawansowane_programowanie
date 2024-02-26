# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
# parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
# ( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
# zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
# tekst "Liczba parzysta" / "Liczba nieparzysta"

def parzysta (a):
    if a%2==0:
        return True
    
def czy_parzysta(liczba):
    if liczba == True:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")

wynik = parzysta(10)

czy_parzysta(wynik)