pixels = []
results = []
with open("dane/dane.txt", "r") as file:
    temp = file.read().splitlines()
    for line in temp:
        linex = line.split(" ")
        linex_int = []
        for el in linex:
            linex_int.append(int(el))
        pixels.append(linex_int)


def zad1():
    min = pixels[0][0]
    max = pixels[0][0]
    for line in pixels:
        for pixel in line:
            if pixel < min:
                min = pixel
            if pixel >= max:
                max = pixel
    print(f"6.1 Najciemniejszy: {min}, najjasniejszy: {max}")
    results.append(f"6.1 Najciemniejszy: {min}, najjasniejszy: {max}")


def zad2():
    nieprawidlowe = []
    for line in pixels:
        flag = False
        for i in range(0, 160):
            if line[i] != line[319-i]:
                flag = True
                break
        if flag:
            nieprawidlowe.append(line)
    print(f"6.2 Lini do usuniecia: {len(nieprawidlowe)}")
    results.append(f"6.2 Lini do usuniecia: {len(nieprawidlowe)}")


def zad3():
    counter = 0
    for i in range(0, len(pixels)):
        for j in range(0, len(pixels[i])):
            current_pixel = pixels[i][j]
            # pixel wyzej
            if i-1 >= 0 and abs(current_pixel - pixels[i - 1][j]) > 128:
                counter += 1
                continue

            # pixel po lewej
            if j - 1 >= 0 and abs(current_pixel - pixels[i][j-1]) > 128:
                counter += 1
                continue

            # pixel ponizej
            if i + 1 < len(pixels) and abs(current_pixel - pixels[i + 1][j]) > 128:
                counter += 1
                continue

            # pixel po prawej
            if j + 1 <= 319 and abs(current_pixel - pixels[i][j+1]) > 128:
                counter += 1
                continue
    print(f"6.3 Pixeli kontrastujacych jest: {counter}")
    results.append(f"6.3 Pixeli kontrastujacych jest: {counter}")


def zad4():
    counter = 0
    wyniki = []
    for j in range(0, 320):
        jasnosc = pixels[0][j]
        for i in range(0, 200):
            if pixels[i][j] == jasnosc:
                counter += 1
            else:
                jasnosc = pixels[i][j]
                wyniki.append(counter)
                counter = 0
    print(f"6.4 Maksymalna dlugosc ciagu: {max(wyniki)}")
    results.append(f"6.4 Maksymalna dlugosc ciagu: {max(wyniki)}")

zad1()
zad2()
zad3()
zad4()

with open("wyniki6.txt", "w") as file:
    for line in results:
        file.write(f"{line}\n")