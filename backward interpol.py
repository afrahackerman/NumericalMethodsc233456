
n = int(input("Number of data points: "))

x = []
y = []

for i in range(n):
    x.append(float(input("Enter x: ")))
    y.append(float(input("Enter y: ")))

target = float(input("Enter target x: "))
h = x[1] - x[0]

for i in range(1, n):
    if abs((x[i] - x[i-1]) - h) > 0.0000001:
        print("X values are not equally spaced.")
        break
else:
    diff = []

    for i in range(n):
        diff.append([y[i]])

    for j in range(1, n):
        for i in range(n - j):
            value = diff[i+1][j-1] - diff[i][j-1]
            diff[i].append(value)

    u = (target - x[n-1]) / h
    result = y[n-1]
    term = 1

    for j in range(1, n):
        term = term * (u + (j-1)) / j
        result = result + term * diff[n-j-1][j]

    print("Interpolated value =", result)
