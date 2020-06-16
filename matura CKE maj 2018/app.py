slowa = []
result = []

with open("dane/sygnaly.txt", "r") as file:
    slowa = file.read().splitlines()


def zad1():
    licznik = 39
    slowo = ""
    while licznik <= len(slowa):
        slowo += slowa[licznik][9]
        licznik += 40
    print(f"4.1 Wiadomosc to: {slowo}")
    result.append(f"4.1 Wiadomosc to: {slowo}")


def zad2():
    ilosc_liter = []
    for slowo in slowa:
        znaki = set(slowo)
        ilosc = len(znaki)
        ilosc_liter.append(ilosc)

    max_liter = max(ilosc_liter)
    print(f"4.2 Slowo: {slowa[ilosc_liter.index(max_liter)]}, liter: {max_liter}")
    result.append(f"4.2 Slowo: {slowa[ilosc_liter.index(max_liter)]}, liter: {max_liter}")


def zad3():
    slowa_warunek = []
    for slowo in slowa:
        flag = True
        for i in range(0, len(slowo)):
            for j in range(0, len(slowo)):
                if abs(ord(slowo[i]) - ord(slowo[j])) > 10:
                    flag = False
        if flag:
            slowa_warunek.append(slowo)
    text = ""
    for slowo in slowa_warunek:
        text += f"\t{slowo} \n"

    print(f"4.3 Slowa spelniajace warunek: {text}")
    result.append(f"4.3 Slowa spelniajace warunek: {text}")


zad1()
zad2()
zad3()

with open("wyniki4.txt", "w") as file:
    for line in result:
        file.write(f"{line}\n\n")