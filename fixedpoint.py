
def g(x):
    return 2 / (x + 1)

x = float(input("Enter initial guess: "))
tol = float(input("Enter tolerance: "))
max_iter = int(input("Maximum iterations: "))

for i in range(1, max_iter + 1):
    new_x = g(x)
    error = abs(new_x - x)

    print(i, new_x, error)

    if error < tol:
        x = new_x
        break

    x = new_x

print("Approximate fixed point =", x)
