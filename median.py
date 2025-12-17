
data = [40, 10, 30, 20, 50]
n = len(data)

for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print("Sorted list:", data)

mid = n // 2

if n % 2 != 0:
    median = data[mid]
else:
    median = (data[mid - 1] + data[mid]) / 2

print("Median:", median)
