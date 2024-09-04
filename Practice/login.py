print("Silahkan Login! \n")

USERNAME = "admin"
PASSWORD = "nimbda123"

inputUsername = input("Username: ")
inputPassword = input("Password: ")

if inputUsername == USERNAME and inputPassword == PASSWORD:
    print("\nBerhasil login!")
else:
    print("\nSalah guoblok!")