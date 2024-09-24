import random

number = random.randint(1, 10)
inputNumber = int(input("Masukan angka: "))

print("\n", number)

if inputNumber > number:
    estimation = inputNumber - number
if inputNumber < number:
    estimation = number - inputNumber

if inputNumber == number:
    print("You're right nigga!")
elif inputNumber < number:
    print(f"You're wrong NIGGA! You're {estimation} a little lower")
else:
    print(f"You're wrong NIGGA! You're {estimation} a little higher")
    