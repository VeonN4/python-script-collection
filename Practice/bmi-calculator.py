h=float(input("Masukan tinggi kamu (m): "))
w=float(input("Masukan berat kamu (kg): "))
 
BMI=w/(h*h)
print("BMI Calculated is:  ",BMI)
 
if(BMI>0):
    if(BMI<=16):
        print("You are very underweight")
    elif(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("Congrats! You are Healthy")
    elif(BMI<=30):
        print("You are overweight")
    else: 
        print("You are very overweight")
else:
    print("Data salah.")