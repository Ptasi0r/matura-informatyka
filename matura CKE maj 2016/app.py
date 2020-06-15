import math


def szyfr_cezara(klucz, slowo):
    litery = "ABCDEFGHIJKLMNQOPRSTUWVXYZ"
    przesuniencie = 0
    if klucz > 26:
        pow = klucz//26
        przesuniencie = klucz - 26*pow
    przesuniencie = klucz
    szyfr = ""
    for letter in slowo:
        if ord(letter) > 90 - przesuniencie:
            szyfr += chr(ord(letter) + przesuniencie - 26)
        else:
            szyfr += chr(ord(letter) + przesuniencie)
    return szyfr

def deszyfr_cezar(klucz, tekst):
    litery = "ABCDEFGHIJKLMNQOPRSTUWVXYZ"
    przesuniencie = 0
    if klucz > 26:
        pow = klucz // 26
        przesuniencie = klucz - 26 * pow
        print(przesuniencie)
    else:
        przesuniencie = klucz
    slowo = ""
    for letter in tekst:
        if ord(letter) < 65 + przesuniencie:
            slowo += chr(ord(letter) + 26 - przesuniencie)
        else:
            slowo += chr(ord(letter) - przesuniencie)
    return slowo


def zad_1():
    words = []
    klucz = 107
    with open("dane/dane_6_1.txt", "r") as file:
        words = file.read().splitlines()
    with open("wyniki_6_1.txt", 'w') as file:
        for word in words:
            file.write(f"{szyfr_cezara(klucz, word)}\n")


def zad_2():
    lines = []
    with open("dane/dane_6_2.txt", "r") as file:
        lines = file.read().splitlines()

    with open("wyniki_6_2.txt", "w") as file:
        for line in lines:
            line = line.split(" ")
            word = line[0]
            try:
                klucz = int(line[1])
            except ValueError:
                klucz = 0
            file.write(f"{deszyfr_cezar(klucz, word)}\n")

def zad_3():
    lines = []
    with open("dane/dane_6_3.txt", "r") as file:
        lines = file.read().splitlines()
    # lines = ["SMIGIELSKI GYUSUQREWU"]
    with open("wyniki_6_3.txt", "w") as file:
        c = 0
        for line in lines:
            line = line.split(" ")
            flag = True
            podstawa = line[0]
            szyf = line[1]

            key = abs(ord(szyf[0]) - ord(podstawa[0]))
            # print(key)
            for i in range(1, len(podstawa)):
                if abs(ord(szyf[i]) - ord(podstawa[i])) != key:
                    # print(abs(ord(szyf[i]) - ord(podstawa[i])))
                    flag = False
                    break
            if flag:
                print(podstawa)

# zad_1()
# zad_2()
zad_3()