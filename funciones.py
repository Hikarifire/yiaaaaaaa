import csv
pedidos = []
precio_5k = 12500
precio_15k = 22500
comunas = ("Santiago", "Colina", "Pirque")

def Registrar_pedido():
    print("REGISTRAR PEDIDO")
    print("CLIENTE")
    rut = int("Ingrese rut: ")
    nombre = input("Ingrese su nombre: ")
    direc = input("Ingrese su dirección: ")
    comuna = int(input("Ingrese comuna(1:Santiago, 2:Colina, 3:Pirque): "))
    print("\nPEDIDO")
    cantidad_5k = 0
    cantidad_15k = 0
    while True: 
        print("Cliente")
        print("1. 5kg - 12.500 ")
        print("2. 15kg - 25.500")
        print("3. Terminar pedido")
        opc2 = input("Indique que cilindro desea agregar al pedido: ")
        if opc2=='1':
            cantidad = int(input("Ingrese cantidad de cilindros de 5kg: "))
            cantidad_5k += cantidad
        elif opc2=='2':
            cantidad = int(input("Ingrese cantidad de cilindros de 15kg: "))
            cantidad_15k += cantidad
        elif opc2=='3':
            break
        else:
            print("ERROR! OPCIÓN INCORRECTA!")
    total = cantidad_5k * precio_5k + cantidad_15k * precio_15k
    pedido = [rut, nombre, direc, comunas[comuna-1], cantidad_5k, cantidad_15k, total]
    pedidos.append(pedido)
    print("PEDIDO CREADO CON ÉXITO!")

def listar_pedidos():
    if not pedidos:
        print("NO EXISTEN PEDIDOS!")
    else:
        print("BUSCAR PEDIDOS")
        rut_buscar = int(input("Ingrese RUT de un cliente a buscar: "))
        tiene_pedidos = False
        for p in pedidos:
            if rut_buscar==p[0]:
                tiene_pedidos=True
                print("RUT:", p[0])
                print("NOMBRE:", p[1])
                print("DIRECCIÓN:", p[2])
                print("COMUNA:", p[3])
                print("CANT. 5K: ", p[4])
                print("CANT. 15KG:", p[5])
                print("TOTAL:", p[6])
                print()
        if not tiene_pedidos:
            print("NO EXISTE: ")

def hoja_ruta():
    if not pedidos:
        print("NO EXISTEN PEDIDOS: ")
    else:
        comuna = int(input("Ingrese número comuna(1:Santiago, 2:Colina, 3:Pirque): "))
        nombre_archivo=input("Ingrese nombre archivo: ") + ".csv"
    try:
        with open(nombre_archivo, "x", newline="") as archivo:
            escritor = csv.writer(archivo)
            for p in pedidos:
                if p[3]==comunas[comuna-1]:
                    escritor.writerow(p)
        print("ARCHIVO CREADO CON ÉXITO!")        
    except:
        print("ERROR! EL NOMBRE DEL ARCHIVO YA EXISTE!")    

def salir():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if len (str(rut)) == 7 in (7,8):
                return rut
            else:
                print("ERROR! DEBE TENER ENTRE 7 O 8 DÍGITOS!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO: ")
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) and nombre.isalpha>=3:
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")