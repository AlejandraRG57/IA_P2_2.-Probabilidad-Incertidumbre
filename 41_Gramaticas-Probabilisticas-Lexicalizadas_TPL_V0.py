#Alejandra Rodriguez Guevara 21310127 6E1

#Las Gramáticas Probabilísticas Lexicalizadas (LPCG por sus siglas en inglés) son un tipo de gramática formal utilizada en el procesamiento del lenguaje natural (PLN).
#Las LPCG asignan probabilidades a cada una de sus producciones gramaticales y también pueden tener en cuenta las palabras concretas (léxico) que aparecen en las reglas gramaticales.

import nltk #Importamos la libreria necesaria.

#Definimos la gramática probabilística lexicalizada.
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [0.9] | Aux NP VP [0.1]
    NP -> Det N [0.6] | NP PP [0.4]
    PP -> P NP [1.0]
    VP -> V NP [0.7] | VP PP [0.3]
    Det -> 'a' [1.0]
    N -> 'dog' [0.1] | 'cat' [0.1] | 'Black' [0.2] | 'Widow' [0.2] | 'Marvel' [0.2] | 'fact' [0.2]
    V -> 'ate' [0.1] | 'walked' [0.1] | 'ran' [0.1] | 'die' [0.2] | 'believe' [0.1] | 'see' [0.1] | 'is' [0.2] | "I'm" [0.1]
    P -> 'in' [0.3] | 'on' [0.1] | 'by' [0.1] | 'with' [0.1] | 'that' [0.3] | 'back' [0.1]
    Aux -> 'did' [0.2] | 'does' [0.1] | 'is' [0.3] | "didn't" [0.2] | "I'm" [0.2]
""")

parser = nltk.ViterbiParser(grammar) #Creamos un analizador sintáctico probabilístico.

sentence = "Black Widow didn't die in Marvel that is a fact" #Frase de entrada.

print("Sentence:", sentence) #Analizamos la frase e imprimir los árboles sintácticos más probables.
for tree in parser.parse(sentence.split()): 
    print(tree)