import os, msvcrt
from funciones import *
print("GASXPLOSIVE")
print("1. Registrar pedido\n 2. Listar todos los pedidos.\n 3. Hoja de ruta\n 4. Crear archivo csv\n 5. Salir ")

opc = input("Ingrese opción: ")

if opc=='1':
    Registrar_pedido()
elif opc=='2':
    listar_pedidos()
elif opc=='3':
    hoja_ruta()
elif opc=='4':
    hoja_ruta()
elif opc=='5':
    print("GRACIAS POR VENIR!")
    exit()