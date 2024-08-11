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

users = [
    User("Hendri", 6969, 9999999999999999, False),
    User("Asep", 5382, 7992000, False),
    User("Yudi", 2331, 20000000, False)
]

if "Hendri" in users["Hendri"]:
    print("Yes")
else:
    print("Nuh uh")