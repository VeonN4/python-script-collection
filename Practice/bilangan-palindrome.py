def palindrome(num: int):
    if num < 0:
        return False
    
    global reversedNum

    reversedNum = 0
    temp = num

    while temp != 0:
        digit = temp % 10
        reversedNum = reversedNum * 10 + digit
        temp //= 10

    return reversedNum == num
    
inputNumber = int(input("Masukan angka: "))
isPalindrome = palindrome(inputNumber)

print(palindrome(inputNumber))

if isPalindrome:
    print(f"Bilangan {inputNumber} adalah Bilangan Palindrome\n")

    print("Input Number:", inputNumber)
    print("Reversed Number:", reversedNum)
else:
    print(f"Bilangan {inputNumber} adalah bukan Bilangan Palindrome\n")