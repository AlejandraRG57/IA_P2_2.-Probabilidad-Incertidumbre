#Alejandra Rodriguez Guevara 21310127 6E1

#La "probabilidad a priori" se refiere a la probabilidad asignada a un evento antes de que se realice cualquier experimento o evidencia empírica. 

class classificador_spam:  #Definimos la clase del clasificador de spam.
    def __init__(self, probabilidad_spam_priori):  #Método inicializador de la clase.
        self.probabilidad_spam_priori = probabilidad_spam_priori  #Almacenamos la probabilidad a priori de que un correo sea spam
    
    def clasificar_correo(self, palabras):  #Método para clasificar un correo como spam o no spam.
        probabilidad_spam = self.probabilidad_spam_priori  #Inicializamos la probabilidad de que el correo sea spam con la probabilidad a priori.

        if probabilidad_spam > 0.5:  #Si la probabilidad de que el correo sea spam es mayor que 0.5
            return "Spam"  #Clasifica el correo como spam.
        else:
            return "No Spam"  #Clasifica el correo como no spam.

probabilidad_spam_priori = 0.3 #Supongamos que tenemos una probabilidad a priori de que un correo sea spam del 30%.

clasificador = classificador_spam(probabilidad_spam_priori) #Creamos una instancia del clasificador spam con la probabilidad a priori especificada.

palabras_correo = ["oferta", "urgente", "promoción"] 
resultado_clasificacion = clasificador.clasificar_correo(palabras_correo)
print("El correo electrónico se clasifica como:", resultado_clasificacion)
