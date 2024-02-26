# Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli
# jedynie parzyste elementy.
import random

def parzyste(liczby):
    for liczba in liczby:
        if liczba%2==0:
            print(liczba)

lista_liczb = [random.randint(0, 100) for i in range(10)]
parzyste(lista_liczb)