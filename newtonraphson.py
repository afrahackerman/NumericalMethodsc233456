def f(x):
    return x*x*x - 6*x + 4

def df(x):
    return 3*x*x - 6

x = float(input("Enter initial guess: "))
tol = float(input("Enter tolerance: "))
max_iter = int(input("Maximum iterations: "))

for i in range(1, max_iter + 1):
    derivative = df(x)

    if abs(derivative) < 0.000000000001:
        print("Derivative is too close to zero.")
        break

    new_x = x - f(x) / derivative
    error = abs(new_x - x)

    print(i,x, f(x), derivative, new_x, error)

    x = new_x

    if error < tol:
        break

print("Approximate root =", x)
