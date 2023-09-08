# practice 🐍

a = (1, 2, 3)
b = list(a)
b[0] = 0
print(a)

##

class myClass:
    def __init__(self, x):
        self.x = x

obj = myClass(42)
print(obj.x)

##

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)
print(list(squares))

##

def multiply(x, y=2):
    return x * y

result = multiply(3)
print(result)

##

s='\n'
print(s.split(),s.splitlines())

##

def cale(arr = [3]):
    arr.append(2)
    return arr

print(sum(cale())+sum(cale()))

##

s = "linkedin"
print(s.replace("in", "is"))