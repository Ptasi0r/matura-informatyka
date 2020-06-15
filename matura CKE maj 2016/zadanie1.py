def suma_dzielnikow(liczba):
    suma_dzielnikow = 1
    for i in range(2, liczba // 2 + 1):
        if liczba % i == 0:
            suma_dzielnikow += i
    return suma_dzielnikow
a = int(input("Podaj liczbe a: "))

suma_dzielnikow_a = suma_dzielnikow(a)
suma_dzielnikow_b = suma_dzielnikow(suma_dzielnikow_a - 1)

if suma_dzielnikow_b-1 == a:
    print("Skojarzone")
else:
    print("Nie")

