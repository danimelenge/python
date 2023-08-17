# Iterar con zip

a = [1, 2, 3, 4, 5, ]
b = ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]
c = zip(a, b)
print(list(c))

##

numeros = [1, 2, 3, 4, 5,]
palabras = ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]
letras = ["A", "B", "C", "D", "E"]
trios = zip(numeros, palabras,letras)
print(list(trios))

##

numeros = [1, 2, 3, 4, 5,]
palabras = ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]
for n, p, in zip(numeros, palabras):
    print("Numeros: ", n)
    print("Palabras: ", p)


##

animal = ["Rana", "Mono", "Pato"]
logetividad = [3, 25, 10]
genero = ["anfibio", "primate", "ana"]

animales = zip(animal, logetividad, genero)

for i in animales:
    print(i)


##

team = ["Texas", "Houston", "Seattle", "LA Angels"]
ganados = [72, 70, 65, 60]
perdidos = [49, 52, 55, 62]

teams = zip(team, perdidos,ganados)

for i in teams:
    print(i)