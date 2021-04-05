num1 = 5
num2 = 3.5
num3 = num1 + num2
print(num3)

a = float(num1)
b = float(num2)
print(f"{a} e {b}")

a = int(float("5.3"))
b = "3.5"
print(f"{a} e {b}")

print("operações")
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(10 / 3) 
print(10 // 3) #divisão arredondamento (floor division)
print(10 % 3) #resto da divisão 
print(2 ** 3) #potenciação

print("operações especiais")
print(abs(-15)) #numero sempre positivo
print(pow(3,3)) #poteniação
print(max(1,5,3)) #num máximo
print(min(1,5,3)) #num mínimo
print(round(8.8)) #arredondamento
print(round(8.5)) #arredondamento
print(round(8.4)) #arredondamento

print("operações biblioteca math")
import math
print(math.floor(8.99999999)) #arredondamento inferior
print(math.ceil(8.00000000000001)) #arredondamento superior
print(math.sqrt(9)) #raix quadrado
