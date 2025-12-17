
data = [2, 4, 5, 2, 6, 4, 2, 5, 4, 4]

frequency = {}

for num in data:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)

mode = max(frequency, key=frequency.get)
print("Mode:", mode)
