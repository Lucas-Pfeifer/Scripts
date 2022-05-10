whileVar = True
while whileVar:
    tipoDeCalculo = int(
        input("Que quieres calcular?\nwatts(1)\nvolts(2)\nampers(3)\nOhms(4)\n..."))

    def watts():
        var01 = int(input("Ingrese la cantidad de watts: "))
        return var01

    def volts():
        var02 = int(input("Ingrese la cantidad de volts: "))
        return var02

    def ampers():
        var03 = (int(input("Ingrese la cantidad de amperaje: ")))
        return var03

    

    if tipoDeCalculo == 1:  # calculo de watts
        print(f"{ampers() * volts()} watts")

    elif tipoDeCalculo == 2:  # calculo de volts
        print(f"{watts() / ampers()} volts")

    elif tipoDeCalculo == 3:  # calculo de ampers
        print(f"{watts() / volts()} ampers")

    elif tipoDeCalculo == 4:  # calculo de Ohms
        print(f"{volts() / ampers()} Ohms")
        
    else:  # error
        print("Ingrese una opcion valida")
    whileVar02 = True
    while whileVar02:
        anotherCalculation = input("Desea continuar? (s/n): ")
        if anotherCalculation == "s":
            whileVar = True
            whileVar02 = False
        elif anotherCalculation == "n":
            whileVar = False
            whileVar02 = False
        else:
            whileVar = False
            print("ingrese una opcion valida")
            whileVar02 = True
