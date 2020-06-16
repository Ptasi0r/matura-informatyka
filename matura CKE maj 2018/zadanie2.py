X = [1, 3, -2, 2]
Y = [3, 4, 2, 1]

def najbardziej_lewy():
    x_naj = 0
    y_naj = 0
    min = X[0]/Y[0]
    for i in range(0, len(X)):
        if X[i]/Y[i] <= min:
            x_naj = X[i]
            y_naj = Y[i]
    print(x_naj, y_naj)

def sortowanie():
    for i in range(0, len(X)-1):
        for j in range(0, len(X)-1):
            if X[j+1]/Y[j+1] < X[j]/Y[j]:
                X[j + 1], Y[j+1], X[j], Y[j] = X[j], Y[j], X[j + 1], Y[j+1]
    print(f"{X}\n{Y}")
najbardziej_lewy()
sortowanie()