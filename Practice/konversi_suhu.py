def promptInput():
    print("Menu Input")

    menu = ["Celcius", "Reamur", "Fahrenheit", "Kelvin"]

    for i in range(len(menu)):
        print(f"{i+1} - {menu[i]}")

    prompt = int(input("Pilih menu (1/2/3/4): "))

    return prompt

def promptOut(inputChoice: int):
    print("\nMenu Output")

    match inputChoice:
        case 1:
            menu = ["Reamur", "Fahrenheit", "Kelvin"]
        case 2:
            menu = ["Celcius", "Fahrenheit", "Kelvin"]
        case 3:
            menu = ["Celcius", "Reamur", "Kelvin"]
        case 4:
            menu = ["Celcius", "Reamur", "Fahrenheit"]
    
    for i in range(len(menu)):
        print(f"{i+1} - {menu[i]}")

    prompt = int(input("Pilih menu (1/2/3/4): "))

    return prompt

def inputTipeSuhu(choice: int):
    inputSuhu = 0

    match choice:
        case 1:
            inputSuhu = "celcius"
        case 2:
            inputSuhu = "reamur"
        case 3:
            inputSuhu = "fahrenheit"
        case 4:
            inputSuhu = "kelvin"

    return inputSuhu


def outputTipeSuhu(inputChoice: int, outputChoice: int):
    outputSuhu = 0

    if inputChoice == 1:
        match outputChoice:
            case 1:
                outputSuhu = "reamur"
            case 2:
                outputSuhu = "fahrenheit"
            case 3:
                outputSuhu = "kelvin"
    elif inputChoice == 2:
        match outputChoice:
            case 1:
                outputSuhu = "celcius"
            case 2:
                outputSuhu = "fahrenheit"
            case 3:
                outputSuhu = "kelvin"
    elif inputChoice == 3:
        match outputChoice:
            case 1:
                outputSuhu = "celcius"
            case 2:
                outputSuhu = "reamur"
            case 3:
                outputSuhu = "kelvin"
    elif inputChoice == 4:
        match outputChoice:
            case 1:
                outputSuhu = "celcius"
            case 2:
                outputSuhu = "reamur"
            case 3:
                outputSuhu = "fahrenheit"
    else:
        print("The choice doesn't exist!")
        return 0
    
    return outputSuhu

def konversi(inputType: str, outputType: str, inputValue: int):
    if inputType == "celcius":
        match outputType:
            case "reamur":
                return (4/5) * inputValue
            case "fahrenheit":
                return (9/5) * inputValue + 32
            case "kelvin":
                return inputValue + 273.15
    elif inputType == "reamur":
        match outputType:
            case "celcius":
                return (5/4) * inputValue
            case "fahrenheit":
                return (9/4) * inputValue + 32
            case "kelvin":
                return (inputValue * (5/4)) + 273.15
    elif inputType == "fahrenheit":
        match outputType:
            case "celcius":
                return 5/9 * (inputValue - 32)
            case "reamur":
                return 4/9 * (inputValue - 32)
            case "kelvin":
                return ((inputValue - 32) / 1.8) + 273.15
    elif inputType == "kelvin":
        match outputType:
            case "celcius":
                return inputValue - 273
            case "reamur":
                return 4/5 * (inputValue - 273)
            case "fahrenheit":
                return 9/5 * (inputValue - 273) + 32
    else:
        return 0

def main():
    print("Program Konversi Suhu\n")

    inputChoice = promptInput()
    outputChoice = promptOut(inputChoice)

    inputType = inputTipeSuhu(inputChoice)
    outputType = outputTipeSuhu(inputChoice, outputChoice)

    inputValue = int(input(f"Masukan nilai input {inputType}: "))

    converted = konversi(inputType, outputType, inputValue)

    print(f"Hasil konversi dari {inputValue} {inputType} adalah: {converted} {outputType}")

if __name__ == "__main__":
    main()