#Alejandra Rodriguez Guevara 21310127 6E1

#El reconocimiento del habla es una tecnología que permite a las computadoras interpretar y entender el lenguaje hablado humano.

import speech_recognition as sr #Importamos el módulo speech_recognition y lo renombramos como sr.

recognizer = sr.Recognizer() #Creamos una instancia del Recognizer.
mic = sr.Microphone() #Creamos una instancia del Microphone.

with mic as source: #Utilizamos el micrófono como fuente de audio.
    audio = recognizer.listen(source) #Escuchamos el audio del micrófono y almacenamos la señal de audio en la variable audio.

text = recognizer.recognize_google(audio, language='ES') #Realizamos el reconocimiento de voz en la señal de audio capturada y almacenamos el texto reconocido en la variable text.

print(f'Has dicho: {text}') #Imprimimos el texto reconocido en la consola.