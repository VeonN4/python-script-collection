class User:
    def __init__(self, name, pin, uang, status):
        self.name   = name
        self.pin    = pin
        self.uang   = uang
        self.status = status

    def deposit(self, inputUang):
        if self.uang - inputUang < 0:
            print("Nuh uh")
            return

        self.uang += inputUang

    def tarik(self, inputUang):
        if self.uang - inputUang < 0:
            print("Nuh uh")
            return

        self.uang -= inputUang

    def changePin(self, newPin):
        if len(newPin) > 4:
            print("Pin jangan melebihi dari 4 angka")
            return
        
        int(newPin)
        self.pin = newPin

def login(user):
    a = True
    foundUser = False

    while a:
        print("\tLOGIN ATM")

        username = input("Masukan Nama: ")

        for i in range(len(user)):
            if username == user[i].name:
                user[i].status = True
                print("Logged in")
                a = False
                foundUser = True

        if not foundUser:
            print("User not found")
    
    return username

def statusCheck(user):
    status = [user for user in user if user.status]

    return status

def display_menu():
    menu = ["Deposit", "Tarik", "Ganti PIN", "Exit"]

    print("\n\tATM MENU\n")

    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

    choice = int(input("\nPilih Menu: "))

    return choice

def deposit(users):
    print("\n\tMenu Deposit")

    user = statusCheck(users)

    print("Saldo:", user[0].uang, "\n")

    inputUang = int(input("Masukan uang yang akan di deposit: "))

    if inputUang <= 0:
        print("Kamu tidak bisa memasukan uang dibawah 0")
        return

    user[0].deposit(inputUang)

def tarik(users):
    print("\n\tMenu Tarik")

    user = statusCheck(users)

    print("Saldo:", user[0].uang, "\n")

    inputUang = int(input("Masukan uang yang akan di tarik: "))

    if inputUang <= 0:
        print("Kamu tidak bisa menarik uang dibawah 0")
        return
    
    user[0].tarik(inputUang)

def changePIN(users):
    print("\n\tMenu Tarik")

    user = statusCheck(users)

    print("Pin sekarang:", user[0].pin, "\n")

    newpin = str(input("Pin baru: "))
    confirmnewpin = str(input("Konfirmasi pin baru: "))

    if newpin == confirmnewpin:
        user[0].changePin(newpin)
    else:
        print("Salah.")

def main():
    users = [
        User("Hendri", 6969, 9999999999999999, False),
        User("Asep", 5382, 7992000, False),
        User("Yudi", 2331, 20000000, False)
    ]

    choice = 0

    loginCheck = login(users)

    statusCheck(users)

    if loginCheck:
        while choice != 4:
            choice = display_menu()
            if choice == 1:
                deposit(users)
            elif choice == 2:
                tarik(users)
            elif choice == 3:
                changePIN(users)
            else:
                return

if __name__ == "__main__":
    main()
