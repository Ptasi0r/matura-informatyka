a = [6, 28, 7, 12, 10, 14, 5, 9, 4, 8, 18]
n = len(a)
p = 7

max1 = 0
max2 = 0
for i in range(0, n):
    if a[i]%p != 0:
        if a[i] > max1:
            max1, max2 = a[i], max1
        elif a[i] > max2:
             max2 = a[i]
print(max1, max2)
print(f"Dla podanego zbioru najwieksze pole to: {max1 * max2}")