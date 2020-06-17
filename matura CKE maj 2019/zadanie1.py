A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]
# A = [1, 5, 6, 8, 12, 16]

#wyszukiwanie binarne - zl. logarytmiczna
lewy = 0
prawy = len(A)

while lewy < prawy:
    srodek = (lewy+prawy)//2
    print("tutaj:", A[srodek], lewy, prawy, A[srodek] < 5)
    if A[srodek]%2 != 0:
    # if A[srodek] < 5:
        lewy = srodek+1
    else:
        prawy = srodek
    print(A[srodek], lewy, prawy)
print(A[prawy])

str(list("abc").reverse())
#wyszukiwanie liniowe
index = 0
for i in range(0, len(A)):
    if A[i]%2 == 0:
        index = i
        break
print(A[index])