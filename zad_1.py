# Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname,
# a następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
# uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie
# go wyświetlić ( print )
def przywitanie(name, surname):
    return f"Cześć {name} {surname}"


imie = "Jan"
nazwisko = "Kowalski"

wynik = przywitanie(imie, nazwisko)
print(wynik)
