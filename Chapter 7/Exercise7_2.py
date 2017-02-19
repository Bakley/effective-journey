def square_root(a):
    x = 5.0
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y


square_root(10)
