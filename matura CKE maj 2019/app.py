import math

potegi_3 = []
liczby = []

i = 0
n = 0
while n <= 100000:
    n = 3**i
    potegi_3.append(n)
    i += 1
# print(potegi_3)

with open("dane/liczby.txt", "r") as file:
    liczby = file.read().splitlines()

def zad1():
    counter = 0
    # print(liczby)
    for liczba in liczby:
        if int(liczba) in potegi_3:
            counter += 1
    print("1.", counter)


def zad2():
    liczby_silnia = []
    for liczba in liczby:
        cyfry = list(liczba)
        suma_silni = 0
        for cyfra in cyfry:
            cyfra = int(cyfra)
            silnia = 1
            for i in range(2, cyfra+1):
                silnia *= i
            suma_silni += silnia
        if suma_silni == int(liczba):
            liczby_silnia.append(liczba)
    print("2. ", liczby_silnia)


def zad3():
    int_liczby = []
    for liczba in liczby:
        int_liczby.append(int(liczba))

    max_ciag = []
    max_dl = 0

    for i in range(0, len(int_liczby)-1):
        ciag = [int_liczby[i], int_liczby[i+1]]
        roznica = math.gcd(int_liczby[i], int_liczby[i+1])
        if roznica == 1:
            continue
        for j in range(i+2, len(int_liczby)):
            if math.gcd(roznica, int_liczby[j]) == roznica:
                ciag.append(int_liczby[j])
            else:
                if len(ciag) > max_dl:
                    max_dl = len(ciag)
                    max_ciag = ciag
                ciag = []
    print(max_ciag)
    print(f"Liczba a1 = {max_ciag[0]}, ilosc wyrazow: {max_dl}, roznica ciagu: {math.gcd(max(max_ciag), min(max_ciag))}")

zad1()
zad2()
zad3()