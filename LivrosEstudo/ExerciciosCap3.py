'''
Exercícios do Capítulo 3
1. Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam
imposto pessoas cujo o salario é maior que R$ 1.000.

2. Escreva uma expressão que sera utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado
o aluno deve ter nota maior ou igual a 7.0. Considere que o aluno cursa apenas 3 materias e que
a nota de cada uma est armazenada nas seguintes variaveis: nota1, nota2 e nota3.

'''

# 1. Verifica se a pessoa deve pagar imposto
salario = 1200  
deve_pagar_imposto = salario > 1000
print(f"Deve pagar imposto: {deve_pagar_imposto}")

# 2. Verifica se o aluno foi aprovado
nota1 = 7.5 
nota2 = 6.0  
nota3 = 8.0 

media = (nota1 + nota2 + nota3) / 3
aprovado = media >= 7.0
print(f"Aluno aprovado: {aprovado}")