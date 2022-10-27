print("")
print("facebook:https://www.facebook.com/Cybersec15")

print("")


print("[1]SUBTRACTION")
print("[2]ADDITION")
print("[3]MULTIPLICATION")
print("[4]DIVISION")
print("[5]MODULUS")
print("[6]FLOOR DIVISION")
print("[7]EXPONENT")

pick = input("ENTER : ")

if pick == "1":
    number1 = input("ENTER NUMBER : ")
    number2 = input("ENTER ANOTHER NUMBER : ")
    result = int(number1) - int(number2)
    print(number1 + " - " + number2 + " = " +  str(result))
    quit()

elif pick == "2":
    num1 = input("ENTER NUMBER : ")
    num2 = input("ENTER ANOTHER NUMBER : ")
    result = int(num1) + int(num2)
    print(num1 + " + " + num2 + " = " + str(result))
    quit()

elif pick == "3":
    num1 = input("ENTER NUMBER : ")
    num2 = input("ENTER ANOTHER NUMBER : ")
    result = int(num1) * int(num2)
    print(num1 + " * " + num2 + " = " + str(result))
    quit()

elif pick == "4":
    num1 = input("ENTER NUMBER : ")
    num2 = input("ENTER ANOTHER NUMBER : ")
    result = int(num1) / int(num2)
    print(num1 + " / " + num2 + " = " + str(result))
    quit()

elif pick == "5":
    num1 = input("ENTER NUMBER : ")
    num2 = input("ENTER ANOTHER NUMBER : ")
    result = int(num1) % int(num2)
    print(num1 + " % " + num2 + " = " + str(result))
    quit()

elif pick == "6":
    num1 = input("ENTER NUMBER : ")
    num2 = input("ENTER ANOTHER NUMBER : ")
    result = int(num1) // int(num2)
    print(num1 + " // " + num2 + " = " + str(result))
    quit()

if pick == "7":
    num1 = input("ENTER NUMBER : ")
    num2 = input("ENTER ANOTHER NUMBER : ")
    result = int(num1) ** int(num2)
    print(num1 + " ** " + num2 + " = " + str(result))
    exit()
