a = 3
b = -4

#OPERADORES ARITMÉTICOS
soma = a + b
sub = a - b
mult = a * b
div = a / b #Divisão em float
div_inteiros = a // b #Divisão em int

print(f"Soma: { soma }")
print(f"Subtração: { sub }")
print(f"Multiplicação: { mult }")
print(f"Divisão: { div }")
print(f"Divisão de inteiros: { div_inteiros }")
print(f"Cálculos dentro do print: { a * b }")
print(f"Resto da divisão de 16 por a: { 16 % a }")

#OPERADORES RELACIONAIS
print(f"a == b: { a == b }")
print(f"a < 5: { a < 5 }")
print(f"a > b: { a > b }")
print(f"a <= 3: { a <= 3 }")
print(f"a >= 4: { a >= 4 }")
print(f"a != b: { a != b }")


#OPERADORES LÓGICOS
logic1 = True
logic2 = False
print(type(logic1))
print(type(logic2))

print(logic1)
print(not logic1)
print(logic1 or logic2)
print(logic1 and logic2)

