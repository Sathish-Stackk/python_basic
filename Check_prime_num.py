num = 17
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

print("Prime" if count == 2 else "Not Prime")
