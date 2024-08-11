class User:
    def __init__(self, name, pin, uang, status):
        self.name   = name
        self.pin    = pin
        self.uang   = uang
        self.status = status

    def increaseUang(self, uang, inputUang):
        self.uang += inputUang

    def changePin(self, pin, newPin):
        self.pin = newPin

def login(user, currentlyLogin):
    username = input("Masukan Nama: ")

    currentlyLogin = []

    for i in range(len(user)):
        a = user[i].name
        if a == username:
            userData = user[i].name, user[i].pin, user[i].status, user[i].uang
            currentlyLogin.append(userData)
            break

    if a != username:
        print("Try again.")

    return currentlyLogin

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
    users = [
        User("Hendri", 6969, 9999999999999999, False),
        User("Asep", 5382, 7992000, False),
        User("Yudi", 2331, 20000000, False)
    ]

    choice = 0

    currentlyLogin = []

    while True:
        loginCheck = login(users, currentlyLogin)
        if loginCheck:
            currentlyLogin.append(loginCheck)
            break

    if loginCheck:
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
