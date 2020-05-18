start_flag = '11011010'
stop_flag = '11010110'
bin_numbers = {
    0: '10101110111010',
    1: '11101010101110',
    2: '10111010101110',
    3: '11101110101010',
    4: '10101110101110',
    5: '11101011101010',
    6: '10111011101010',
    7: '10101011101110',
    8: '11101010111010',
    9: '10111010111010',
}

codes = []
checksum_codes = []
with open('dane/kody.txt', 'r') as file:
    codes = file.read().splitlines()

# suma cyfr liczy:
with open('kody1.txt', 'w') as file:
    for code in codes:
        sum_even = 0
        sum_odds = 0
        code = reversed(code)
        for index, letter in enumerate(code):
            letter = int(letter)
            if index%2 == 0:
                sum_even += letter
            else:
                sum_odds += letter
        sum_even *= 3
        file.write(f'{sum_even} {sum_odds} \n')

        #oblicznie sumy kontorlnej
        suma = sum_even + sum_odds
        reszta = suma%10
        wynik = 10 - reszta
        reszta = wynik%10
        checksum_codes.append(reszta)

with open('kod2.txt', 'w') as file:
    for checksum in checksum_codes:
        file.write(f'{checksum} {bin_numbers[checksum]} \n')

# zapis calej liczby w systemie Standard Code 35
with open('kod3.txt', 'w') as file:
    for code, checksum in zip(codes, checksum_codes):
        stncode25 = start_flag
        for letter in code:
            stncode25 += bin_numbers[int(letter)]
        stncode25 += bin_numbers[checksum]
        stncode25 += stop_flag
        file.write(f'{stncode25} \n')
