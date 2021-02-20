import serial

# Inicializamos el puerto de serie a 9600 baud
ser = serial.Serial('COM3', 9600)

# Mostramos un mensaje para que el usuario introduzca un valor o la letra "s" para salir del bucle
print("Introduce un numero entre 0-180, o 's' para salir del programa\n")

# Guardamos el numero en una variable
entrada = input()

# Introduciendo 's' salimos del bucle
while entrada != 's':

    # Si el numero es valido, se envia por serial
    if (int(entrada) >= 0 and int(entrada) <= 180):

        # Enviamos el numero por serial, codificado en Unicode
        ser.write(str(entrada).encode())

        # Mostramos el numero enviado por pantalla
        print("He enviado: " + str(entrada))

    # Si el numero no es valido, mostramos un mensaje de error
    else:
        print("Error: introduce un numero entre 0-180, o 's' para salir")

    # Pedimos un nuevo numero al usuario
    print("Introduce un numero entre 0-180: ")
    entrada = input()

