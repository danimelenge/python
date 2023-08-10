## DaniM Python 🐍

class Alumno:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        
        print(f"¡Hola, {self.nombre}!")


alumno = Alumno("Pablo")
alumno.saludar()


class Perro:

    def __init__(self, name):
        self.name = name

    def greeting(self):

        print(f"Hello, {self.name}!")

perro = Perro("cloe")
perro.greeting()


class   Woman:

    def __init__(self, name):
        self.name = name

    def greeting(self):
    
            print(f"Hello, I'm {self.name}!")


woman = Woman("Romi")
woman.greeting()


# ####

import json

data = {
    "name": "David",
    "age": 28,
    "city": "Cali",
    "ID": 2345867,
    "State": "Valle"
}

y = json.dumps(data)

print(y)


# ###

 import json


data = {
    "name": "Luis Castillo",
    "age": 30,
    "city": "Seattle",
    "estatura": 1.88,
    "peso": "90kg",
    "team": "Mariners"
}

y = json.dumps(data)

print(y)
print(data["peso"])
print(data["estatura"])
print(data["team"])

# ###

import json


data = {
    "name": "Shohei Ohtani",
    "age": 29,
    "city": "Oshu",
    "estatura": 1.93,
    "peso": "95kg",
    "team": "Angels"
}

y = json.dumps(data)

print(data["team"])
print(data["peso"])
print(data["estatura"])
print(data["city"])
print(data["name"])

# ####

s = '\n'
print(s.split(),s.splitlines())

# ###

li = [10,20,30,40]
li[1:3] = [50]
print(li)

# ###

lst =[1,2,3,4,5]
for i in lst:
    if i == 3:
        break
    print(i)
else:
    print("Completed successfully")

# ####

a=(1 << 53)+1
print(a+1.0 > a)

# ######

a = "Hello"
b = a.replace("l", "L", 1)
print(b)

# #####

def foo(a, b=2, c=3):
    return  a + b + c
print(foo(c=1, a=3))

# ####

x = 10
y = 2
result = x % y == 0
print(result)

# #####

def my_func(a, b):
    return  a + b

result  = my_func(2, 3) * 2
print(result)

# #####

x = 10
y = 5
result = (x > y) or (y < 2) and (x == 10)
print(result)

# #####

my_dict = {1: "one", 2: "two", 3: "three"}
result = "three" in  my_dict.values()
print(result)

# Russian Multiplication 🇷🇺

multiplicando = int(input("Ingrese el multiplicador: "))
multiplicador = int(input("Ingrese el multiplicando: "))

acum = 0

while multiplicando >= 1:
    if multiplicando % 2 != 0:

        acum = acum + multiplicador
    multiplicando = multiplicando // 2
    multiplicador = multiplicador * 2
print(f"La respuesta es: {acum}")
