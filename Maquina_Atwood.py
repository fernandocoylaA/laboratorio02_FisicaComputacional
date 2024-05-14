def maquinaAtwood():
    g = 9.8 #gravedad
    m1 = float(input("Ingrese la masa 1 (kg): "))
    m2 = float(input("Ingrese la masa 2 (kg): "))
    if(m1 == m2):
        print("Sistema en equilibrio, no existe aceleracion")
        tension = round((m1 * g),2) #redondear a dos decimales
        print("Tension de la cuerda es : " + str(tension) + " N")
    elif(m1>m2):
        #se halla la aceleracion
        acel = round(g * ((m1 - m2)/(m1 + m2)) , 2) #redondear a dos decimales
        tension = round(m2 * (acel + g) , 2) #redondear a dos decimales
        print("La aceleracion es: "+ str(acel) +" m/s^2")
        print("La tension en la cuenda es: "+ str(tension)+" N")
    elif(m2>m1):
        #se halla la aceleracion
        acel = round(g * ((m2 - m1)/(m2 + m1)) , 2) #redondear a dos decimales
        tension = round(m1 * (acel + g) , 2) #redondear a dos decimales
        print("La aceleracion es: "+ str(acel) +" m/s^2")
        print("La tension en la cuenda es: "+ str(tension)+" N")
    


# Menu de Opciones
def menu():
    print("** ::::::::::::::::::::::::: **")
    print("::       Maquina de Atwood    ::")
    print("** ::::::::::::::::::::::::: **")
    print("-------------------------------")
    print("| Ingresar:            ->  1   |")
    print("| Salir:               ->  s   |")
    print("--------------------------------")
    print("** ::::::::::::::::::::::::: **")
    print("\n")

#Opcion seleccionada
def opciones():
   opcion = input("Seleccione una Opción... ")
   return opcion

def errorOperacion():
    regresar = input("¿Quiere realizar una nueva operación [S/N]? ")
    return regresar

while True:
    menuOpciones = menu() #mostrar menu de opciones
    opc = opciones() 

    #opcion para salir 
    if opc =='s':
        print("Saliendo...")
        break

    #Opcion Maquina Atwood
    elif opc == '1':
        print("\n")
        print("**            Maquina de Atwood            **") 
        print("*Mediante el ingreso del peso de dos Objetos*")
        print("*Se hallará la aceleracion y la tension en el Sistema*")                
        maquinaAtwood()      
        nuevaOperacion = errorOperacion()     

    #Opcion incorrecta    
    else:
        print("Opción no válida")
        continue

    #Opcion para salir
    if nuevaOperacion.upper() != "S" :
        print("Saliendo...")
        break