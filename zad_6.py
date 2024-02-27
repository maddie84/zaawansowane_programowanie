# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
# list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
# duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
# powstałą listę.

def listy(lista1 = [], lista2 = []):
    lista_polaczona = lista1 + lista2

    unikalna_lista = list(set(lista_polaczona))

    przetworzona_lista = [element**3 for element in unikalna_lista]
    
    return przetworzona_lista

lista_a = [1, 2, 3, 4]
lista_b = [3, 4, 5, 6]

print(listy(lista_a, lista_b))

