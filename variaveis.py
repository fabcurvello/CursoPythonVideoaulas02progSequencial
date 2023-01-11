pais = "Brasil"
numero = 10
casado = True

nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))
salario = float(input("Informe o seu salário: "))

print(type(pais))
print(type(numero))
print(type(casado)) # tipo bool -> booleano ou lógico (verdadeiro ou falso)
print(type(nome))
print(type(idade))
print(type(salario))

nota1 = float(input("Informe a sua nota 1: "))
nota2 = float(input("Informe a sua nota 2: "))

media = (nota1 + nota2) / 2
print("A sua média é ", media)