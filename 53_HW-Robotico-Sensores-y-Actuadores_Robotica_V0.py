#Alejandra Rodriguez Guevara 21310127 6E1

#En el diseño de hardware para robótica, los sensores y actuadores son componentes fundamentales que permiten a los robots percibir su entorno y actuar en él.

import serial
import time

#Configuramos la conexión serial con el Arduino.
arduino_port = '/dev/ttyUSB0'  #Cambiamos al puerto correcto donde esté conectado nuestro Arduino.
baud_rate = 9600

arduino = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  #Esperamos a que se establezca la conexión.

try:
    while True:
        #Enviamos un mensaje al Arduino para solicitar la lectura del sensor.
        arduino.write(b'read_sensor\n')

        #Leemos la respuesta del Arduino.
        response = arduino.readline().decode().strip()

        #Imprimimos la respuesta.
        print("Lectura del sensor:", response)

        time.sleep(0.5)  #Esperamos un momento antes de solicitar la próxima lectura.

except KeyboardInterrupt:
    print("Programa terminado por el usuario")
    arduino.close()