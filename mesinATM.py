class User:
    def __init__(self, name, pin, uang):
        self.name   = name
        self.pin    = pin
        self.uang   = uang

    def increaseUang(self, uang, inputUang):
        self.uang += inputUang

    def changePin(self, pin, newPin):
        self.pin = newPin

def login(user):
    username = str(input("Masukan nama: "))

    if username == 

def display_menu():
    menu = ["Deposit", "Tarik", "Change PIN", "Exit"]

    print("\tATM MENU")

    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

    choice = int(input("Select Menu: "))

    return choice

def deposit(users):
    print("\tMenu Deposit")

    

def tarik(uang):
    pass

def changePIN(pin):
    pass

def main():
    users = {
        User("Hendri", 6969, 9999999999999999),
        User("Asep", 5382, 7992000),
        User("Yudi", 2331, 20000000)
    }

    choice = 0

    while True:
        choice = display_menu()
        if choice == 1:
            deposit(users)
        elif choice == 2:
            tarik()
        elif choice == 3:
            changePIN()
        else:
            exit()

if __name__ == "__main__":
    main()
