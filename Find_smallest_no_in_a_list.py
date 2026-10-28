numbers = [34, 12, 56, 8, 25]

smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n

print("Smallest:", smallest)
