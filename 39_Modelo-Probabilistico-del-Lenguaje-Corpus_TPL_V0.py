#Alejandra Rodriguez Guevara 21310127 6E1

#Un modelo probabilístico del lenguaje es una representación matemática de la probabilidad de ocurrencia de secuencias de palabras en un lenguaje natural. 
#Para crear un modelo probabilístico del lenguaje, necesitas un corpus, que es un conjunto de textos en el idioma de interés.

class Corpus:
    def __init__(self, texts):
        self.texts = texts #Inicializamos el corpus con una lista de textos.
    
    def tokenize(self, text): #Tokenizamos un texto en palabras.
        return text.split() #Lo dividimos por espacios en blanco
    
    def preprocess(self): #Tokenizamos y preprocesamos cada texto en el corpus.
        self.tokenized_texts = [self.tokenize(text.lower()) for text in self.texts] #Convertimos las palabras a minúscula.
    
    def ngram(self, n): #Generamos n-gramas de palabras a partir de los textos tokenizados.
        ngrams = []
        for tokens in self.tokenized_texts:
            for i in range(len(tokens) - n + 1):
                ngrams.append(tuple(tokens[i:i+n])) #Agregamos el n-grama a la lista como una tupla.
        return ngrams


texts = [
    "Black Widow didn't die.",
    "You don't even believe that.",
    "And when I'm back in Chicago, I feeeel it."
    "When I see you again oooooooooooooooooooh."
]

corpus = Corpus(texts)
corpus.preprocess()  #Tokenizamos y preprocesamos los textos del corpus.
print(corpus.tokenized_texts)  #Imprimimos los textos tokenizados.
print(corpus.ngram(2))  #Imprimimos los bigramas generados a partir de los textos tokenizados.
