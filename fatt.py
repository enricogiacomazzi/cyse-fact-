


def fattoriale(n):
    if n == 0:
        return 2
    else:
        return n * fattoriale(n - 1);



print(fattoriale(5))