import os
import numpy as np
from colorama import Fore, Back, Style

#init()

avion = np.zeros(42, dtype=int)
nombres = [""] * 42
ruts = [""] * 42
fonos = [""] * 42
bancos = [""] * 42
    
def pedirDatos():
    asiento = int(input("asiento a comprar: "))
    if avion[asiento-1] != 0:
        print("Asiento ocupado")
    else:
        nombres[asiento-1] = input("nombre: ")
        ruts[asiento-1] = input("rut con guion: ")
        fonos[asiento-1] = input("telefono: ")
        bancos[asiento -1] = input("banco [bancoduoc tiene 15% descuento]: ")
        if asiento < 31:
            avion[asiento-1] = 72000
        else:
            avion[asiento-1] = 240000
        if bancos[asiento-1] == "bancoduoc":
             avion[asiento-1] *= 0.85

def devolverAsiento():
    asiento = int(input("asiento a devolver: "))
    if avion[asiento-1] == 0:
        print("Asiento vacío, no se puede anular")
    else:
        avion[asiento-1] = 0
        nombres[asiento-1] = ""
        ruts[asiento-1] = ""
        fonos[asiento-1] = ""
        bancos[asiento-1] = ""
        
def modificarAsiento():
    asiento = int(input("asiento a modificar: "))
    rut = input("rut del asiento comprado: ")
    
    if avion[asiento-1] != 0 and ruts[asiento-1] == rut:
        nombres[asiento-1] = input("nombre: ")
        fonos[asiento-1] = input("nuevo telefono: ")
    else:
        print("asiento no vendido o no corresponde con rut ingresado")
        
        
    if avion[asiento-1] == 0:
        print("Asiento vacío, no se puede anular")
    else:
        nombres[asiento-1] = ""
        ruts[asiento-1] = ""
        fonos[asiento-1] = ""
        bancos[asiento-1] = ""


def mostrarAvion():
    print(f"\n    {Fore.CYAN}--------- NORMAL ---------{Style.RESET_ALL}", end="")
    for i in range(len(avion)):
        if(i==30):
            print(f"\n\n    {Fore.YELLOW}{Style.BRIGHT}---------- VIP ----------{Style.RESET_ALL}{Style.BRIGHT}", end="")
        if(i % 6 == 0):
            print("")
            print("")
        if(i % 3 == 0):
            print("   ", end="")
        if(avion[i] != 0):
            print(f"{Fore.RED}{Style.BRIGHT}  X {Style.RESET_ALL}", end="" )
        else:
            print(f" {(i+1):2d} ", end="")
    print("\n\n")

def menu():
    
    print("""  MENU
          1. Ver asientos disponibles
          2. Comprar asiento
          3. Anular asiento
          4. Modificar datos
          5. salir
          """)
    return input("Digite opcion: ")



# principal


while True:
    os.system("cls")
    opcion = menu()

    if opcion == "1":
        mostrarAvion()
    elif opcion == "2":
        mostrarAvion()
        pedirDatos()
    elif opcion == "3":
        devolverAsiento()
    elif opcion == "4":
        modificarAsiento()
    elif opcion == "5":
        break
            
    input(f"{Style.RESET_ALL}Presione {Fore.GREEN}[Enter]{Style.RESET_ALL} para continuar")

print("vale vale mi waxoo 🤑🤙")
