#Alejandra Rodriguez Guevara 21310127 6E1

#La traducción automática estadística es un enfoque de traducción automática que se basa en modelos estadísticos entrenados a partir de ejemplos de traducción. 
#En este método, se utiliza un gran corpus de textos paralelos en dos idiomas para aprender la relación entre las palabras y las frases en ambos idiomas. 
#Luego, estos modelos estadísticos se utilizan para traducir automáticamente textos de un idioma a otro.

from googletrans import Translator #Usamos la libreria de google translator.

translator = Translator()

#Traducimos el texto "Me gustan los libros" al inglés.
print(translator.translate("Me gustan los libros", dest="en"))