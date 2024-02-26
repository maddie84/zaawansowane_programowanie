# Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
# drugi element.
import random 

def co_druga(liczby):
    for indeks in range(0, len(liczby), 2):
        print(liczby[indeks])

lista_liczb = [random.randint(0, 100) for i in range(10)]
co_druga(lista_liczb)