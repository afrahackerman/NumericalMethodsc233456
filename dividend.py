n = int(input("Number of data points: "))

x = []
y = []

for i in range(n):
    x.append(float(input("Enter x: ")))
    y.append(float(input("Enter y: ")))

target = float(input("Enter target x: "))

dd = []

for i in range(n):
    dd.append([y[i]])

for j in range(1, n):
    for i in range(n - j):
        denominator = x[i+j] - x[i]

        if denominator == 0:
            print("Duplicate x values are not allowed.")
            raise SystemExit

        value = (dd[i+1][j-1] - dd[i][j-1]) / denominator
        dd[i].append(value)

result = dd[0][0]
product = 1

for j in range(1, n):
    product = product * (target - x[j-1])
    result = result + dd[0][j] * product

print("Interpolated value =", result)
