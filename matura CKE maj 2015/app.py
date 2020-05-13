numbers = []
answers = []

with open('Dane/liczby.txt', 'r') as file:
    numbers = file.read().splitlines()

numbers_dec = [int(number, 2) for number in numbers]


def more_zeros_than_ones():
    counter = 0
    for number in numbers:
        if number.count('0') > number.count('1'):
            counter += 1
    print(f"Zad. 4.1 W pliku znajduje się {counter} liczb które posiadają więcej 0 niż 1 ")
    answers.append(f"Zad. 4.1 W pliku znajduje się {counter} liczb które posiadają więcej 0 niż 1 ")


def divided_by_two_or_eight():
    counter_2 = 0
    counter_8 = 0
    for number in numbers_dec:
        if number%8 == 0:
            counter_2 += 1
            counter_8 += 1
        elif number%2 == 0:
            counter_2 += 1
    print(f"Zad. 4.2 W pliku znajduje się {counter_2} liczb podzielnych przez 2, oraz {counter_8} liczb podzielnych przez 8")
    answers.append(f"Zad. 4.2 W pliku znajduje się {counter_2} liczb podzielnych przez 2, oraz {counter_8} liczb podzielnych przez 8")

def minimum_and_maxiumum_value():
    min_value = numbers_dec.index(min(numbers_dec)) + 1
    max_value = numbers_dec.index(max(numbers_dec)) + 1
    print(f"Zad. 4.3 Najmniejsza liczba znajduje się w lini: {min_value}, a największa w lini: {max_value}")
    answers.append(f"Zad. 4.3 Najmniejsza liczba znajduje się w lini: {min_value}, a największa w lini: {max_value}")


more_zeros_than_ones()
divided_by_two_or_eight()
minimum_and_maxiumum_value()

with open('wynik4.txt', 'w') as file:
    for answer in answers:
        file.write(answer + "\n")