def szyfr_cezara(klucz, slowo):
    litery = "ABCDEFGHIJKLMNQOPRSTUWVXYZ"
    przesuniencie = 0
    if klucz > 26:
        pow = klucz//26
        przesuniencie = klucz - 26*pow
        print(przesuniencie)
    szyfr = ""
    for letter in slowo:
        print(ord(letter), letter)
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
        # print(przesuniencie)

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
    print(lines[-1])

    with open("wyniki_6_2.txt", "w") as file:
        for line in lines:
            line = line.split(" ")
            word = line[0]
            klucz = int(line[1])
            # print(line)
            file.write(f"{deszyfr_cezar(klucz, word)}\n")

# zad_1()
zad_2()