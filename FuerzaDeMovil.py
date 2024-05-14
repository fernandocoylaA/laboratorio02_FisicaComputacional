
import matplotlib.pyplot as plt

def fuerzaMovil():
    masa = float(input("Ingrese la Masa(kg): "))
    if(masa <= 0 ):
        print("Masa debe ser mayor y distinto de cero")   
        return 0
    velFin= float(input("Ingrese la velocidad final (m/s): "))
    velIni = float(input("Ingrese la velocidad inicial (m/s): ")) 
    if(velIni < 0):
        print("La velocidad inicial no puede ser Negativa!") 
        return 0
    tiempo = float(input("Ingrese el tiempo (segundos): "))
    if(tiempo <= 0):
       print("El tiempo no puede ser negativo o cero")
       return 0
    else:
        resultado = round(abs(masa * ((velFin - velIni) / tiempo)) , 4)  
        print("La fuerza que describe el movil es: "+str(resultado)+" N")       
        #grafica
        plt.plot([0,tiempo],[velIni,velFin])
        plt.title('Cambio de velocidad')
        plt.xlabel('Tiempo(s)')
        plt.ylabel('Velocidad(m/s)')
        plt.show()       
        

# Menu de Opciones
def menu():
    print("** ::::::::::::::::::::::::: **")
    print("::   Calcular FUERZA DE UN MOVIL ::")
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

    #Opcion FUERZA MOVIL
    elif opc == '1':
        print("\n")
        print("**       FUERZA MOVIL     **") 
        print("En este programa:")
        print("*Calcularemos la fuerza del Movil y mostraremos su grafica*")                       
        fuerzaMovil()    
        nuevaOperacion = errorOperacion()     

    #Opcion incorrecta    
    else:
        print("Opción no válida")
        continue

    #Opcion para salir
    if nuevaOperacion.upper() != "S" :
        print("Saliendo...")
        break