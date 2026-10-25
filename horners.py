
# f(x) = 2x^3 - 6x^2 + 2x - 1

x = float(input("Enter x: "))

a = [3,-5,0,4,-6]
result = a[0]

for i in range(1, len(a)):
    result = result * x + a[i]
    print(result)

print("Polynomial value =", result)
