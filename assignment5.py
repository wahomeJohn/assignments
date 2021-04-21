def options():
    print("[P] Print Options")
    print("[C] convert from celsius")
    print("[F] Covert from Fahrenheit" )
    print("[M] Convert from Miles")
    print("[KM] Convert from Kilometers")
    print("[In] Convert from Inches")
    print("[CM] Convert from centimeters")
    print("[Q]")

def PrintOptions():
    options()

options()
option = input("option :")
while option != 'Q':
    if option == 'P':
        PrintOptions()
        print()

    elif option == 'C':
        c = float(input("Enter temperature in celsius :"))
        f = (c * 1.8000) + 32
        print("Celsius temperature :",c)
        print("Fahrenheit:",f)
        print()

    elif option == 'F':
        f = float (input("Enter temperature in Fahrenheit :"))
        c = (f-32)/1.800
        print("Fahrenheit temperature :", c)
        print("Celsius:", f)
        print()

    elif option == 'M':
        m = float(input("Enter distance in Miles :"))
        km = (m/0.62137)
        print("Miles distance :", m)
        print("Kilometer:", km)
        print()

    elif option == 'KM':
        km = float(input("Enter distance in kilometers :"))
        m = km * 0.62137
        print("Kilometers distance :", km)
        print("Miles:", m)
        print()

    elif option == 'In':
        inc = float(input("Enter length in Inches :"))
        cm = (inc / 0.39370)
        print("Inches length :", inc)
        print("Centimeter:", cm)
        print()

    elif option == 'CM':
        cm = float(input("Enter length in centimeters :"))
        inc = cm * 0.39370
        print("Centimeter length :", cm)
        print("Inches:", inc)
        print()

    else:
        print("Invalid option")

    #options()
    option = input("option :")