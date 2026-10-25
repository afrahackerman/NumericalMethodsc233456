
def f(x):
    return 2*x*x*x - 2*x - 5

x0 = float(input("Enter first guess: "))
x1 = float(input("Enter second guess: "))
tol = float(input("Enter tolerance: "))
max_iter = int(input("Maximum iterations: "))

for i in range(1, max_iter + 1):
    f0 = f(x0)
    f1 = f(x1)

    denominator = f1 - f0

    if abs(denominator) < 0.000000000001:
        print("Denominator is too close to zero.")
        break

    x2 = x1 - f1 * (x1 - x0) / denominator
    error = abs(x2 - x1)

    print(i,x0, x1,f(x0),f(x1),x2, error)

    x0 = x1
    x1 = x2

    if error < tol:
        break

print("Approximate root =", x2)
