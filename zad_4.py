# Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
# dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
# informację jako typ logiczny bool

def suma(a, b, c):
    if (a + b >= c):
        return True
    else:
        return False
    
print(suma(1,1,3))