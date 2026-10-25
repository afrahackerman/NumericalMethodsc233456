def f(x):
    return x*x - 4*x - 10

a = float(input("Enter a: "))
b = float(input("Enter b: "))
tol = float(input("Enter tolerance: "))
max_iter = int(input("Maximum iterations: "))

if f(a) * f(b) >= 0:
    print("Invalid interval: no sign change.")
else:
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        print(i, a, b, c, fc)

        if abs(fc) < tol or abs(b - a) / 2 < tol:
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("Approximate root =", c)

