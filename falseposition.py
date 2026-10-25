
def f(x):
    return x*x*x - 7*x + 4

a = float(input("Enter a: "))
b = float(input("Enter b: "))
tol = float(input("Enter tolerance: "))
max_iter = int(input("Maximum iterations: "))

if f(a) * f(b) >= 0:
    print("Invalid interval: no sign change.")
else:
    for i in range(1, max_iter + 1):
        fa = f(a)
        fb = f(b)

        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        print(i, a, b, c, fc)

        if abs(fc) < tol:
            break

        if fa * fc < 0:
            b = c
        else:
            a = c

    print("Approximate root =", c)
