peso = float(input("peso: "))
altura = float(input("altura: "))

x = peso / (altura ** 2)
if x < 18.5:
    print("bajo de peso")
elif x >= 18.5 and x < 25:
    print("peso normal")
elif x >= 25 and x < 30:
    print("sobre peso")
elif x > 30:
    print("obesidad")
print(str(x) + " Es tu indice de masa corporal")
