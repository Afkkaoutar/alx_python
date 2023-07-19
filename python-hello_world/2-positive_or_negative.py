   #!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

print(number, end=" ")

if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")  