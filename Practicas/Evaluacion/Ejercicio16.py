#TODO: PARTIENDO DE UNA FRASE IMPRIMIR PALABRA POR PALABRA Y UN CONTADOR DE PALABRAS TOTALES
from os.path import split

word = input("Enter the text:")

words = word.split( )

for wordss in words:
    print(wordss)

countWords = 0

i = 0
for i in words:
    countWords += word.count(i)

print(f"\nThe total words are: {countWords}")