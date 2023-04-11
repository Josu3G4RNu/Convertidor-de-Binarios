"""Sistema para la transformación de direcciones ip a binario
Ejemplo:
211.111.111.1 -> 11010011.01101111.01101111.000000001

El sistema habrá de leer las direcciones de un archivo txt de nombre
cualquiera, todo con el fin de agilizar la lectura y transformación
de estas. Al final el sistema habrá de sobrescribir la información con
las transformaciones binarias como en el ejemplo.
"""


def lectura_archivo(nombre_archivo):
    """Abre el archivo en modo lectura
    
    :param: nombre_archivo: dirección del archivo a consultar
    :return: lista con las direcciones ip a transformar
    """
    try:
        archivo = open(nombre_archivo, "r")
    except:
        op = input("No se encontró el archivo, desea crearlo? (s/n)").lower()
        if op == "s":
            archivo = open(nombre_archivo, "w")
            archivo.write("Dirección IP".format("%16s") + "\n")
            archivo.close()
            lectura_archivo(nombre_archivo)
        else:
            print("No se pudo abrir el archivo")
    else:
        direcciones = archivo.readlines()
        direcciones.pop(0)
        for i in range(len(direcciones)):
            direcciones[i] = direcciones[i].split("->")
            direcciones[i] = direcciones[i][0].strip()
        return direcciones


def transformación_binaria(list_direcciones):
    """Transforma las direcciones ip a binario
    
    :param: list_direcciones -> lista con las direcciones ip a transformar
    :return -> lista con las direcciones ip transformadas a binario
    """
    list_binarios = []
    for ip in list_direcciones:
        di = ip.rstrip("\n").split(".")
        binario = ""
        for i in range(len(di)):
            num = int(di[i])  # Separación de los números que conforma la dirección ip)
            b = ""
            while num > 0:
                b += str(num % 2)
                num = num // 2
            while len(b) < 8:
                b += "0"
            b = "." + b
            binario += b[::-1]
        list_binarios.append(binario)
    return list_binarios


def escritura_archivo(nombre_archivo, list_direcciones, list_binarios):
    """Sobrescribe el archivo con las direcciones ip transformadas a binario
    
    param: nombre_archivo -> dirección del archivo que ha de sobreescribirse
    param: list_direcciones -> lista con las direcciones ip a transformar
    param: list_binarios -> lista con las direcciones ip transformadas a binario
    """
    try:
        archivo = open(nombre_archivo, "w")
    except:
        print("El archivo no se encuentra verifica la ruta")
    else:
        archivo.write("{:<16} -> {:<32}\n".format("Dirección IP", "Dirección Binaria"))
        for ip, ipb in zip(list_direcciones, list_binarios):
            cadena = "{:<16} -> {:>5}\n".format(ip, ipb.rstrip("."))
            archivo.write(cadena)
        archivo.close()


if __name__ == '__main__':
    list_direcciones = lectura_archivo("Prueba.txt")
    list_binarios = transformación_binaria(list_direcciones)
    escritura_archivo("Prueba.txt", list_direcciones, list_binarios)
    print("Conversiones realizadas con éxito")
