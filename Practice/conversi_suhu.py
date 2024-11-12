def inputTipeSuhu(choice):
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

def promptInput():
    menu = ["Celcius", "Reamur", "Fahrenheit", "Kelvin"]

    for i in range(len(menu)):
        print(f"{i+1} - {menu[i]}")

    prompt = int(input("Pilih menu (1/2/3/4): "))

    return prompt

def ouputTipeSuhu(choice):
    outputSuhu = 0

    match choice:
        case 1: