#Alejandra Rodriguez Guevara 21310127 6E1

#Las Gramáticas de Probabilidad Independiente del Contexto (PCFG, por sus siglas en inglés) son un tipo de modelo probabilístico utilizado en 
#el procesamiento del lenguaje natural. Permiten modelar la probabilidad de una secuencia de símbolos dado un árbol de análisis sintáctico.

import nltk #Importamos las librerias necesarias.
from nltk import PCFG, Nonterminal, ProbabilisticProduction

productions = [ #Definimos algunas producciones gramaticales con sus respectivas probabilidades.
    ProbabilisticProduction(Nonterminal('S'), ['NP', 'VP'], prob=0.9),
    ProbabilisticProduction(Nonterminal('S'), ['Aux', 'NP', 'VP'], prob=0.1),
    ProbabilisticProduction(Nonterminal('NP'), ['Det', 'N'], prob=0.6),
    ProbabilisticProduction(Nonterminal('NP'), ['NP', 'PP'], prob=0.4),
    ProbabilisticProduction(Nonterminal('PP'), ['P', 'NP'], prob=1.0),
    ProbabilisticProduction(Nonterminal('VP'), ['V', 'NP'], prob=0.7),
    ProbabilisticProduction(Nonterminal('VP'), ['VP', 'PP'], prob=0.3),
]

#-> S: Representa una oración completa.
#-> NP: Sintagma nominal, que representa un grupo de palabras que funcionan juntas como un sustantivo.
#-> VP: Sintagma verbal, que representa un grupo de palabras que funcionan juntas como un verbo.
#-> Aux: Auxiliar.
#-> Det: Determinante.
#-> N: Sustantivo, que representa una palabra que denota una persona, lugar, cosa o idea.
#-> PP: Frase preposicional, que representa un grupo de palabras que comienza con una preposición y generalmente incluye un sustantivo o un sintagma nominal.
#-> P: Preposición.
#-> V: Verbo, que representa palabras que expresan acción, estado o condición. 

grammar = PCFG(Nonterminal('S'), productions) #Creamos la gramática PCFG.

print(grammar) #Imprimimos la gramática.

rd_parser = nltk.ViterbiParser(grammar) #Generamos una frase aleatoria según la gramática.
for tree in rd_parser.parse(['Det', 'N', 'V', 'Det', 'N']):
    print(tree)