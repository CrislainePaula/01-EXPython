# Entrada de dados
salario_atual = float(input("Informe o salário atual: R$ "))
percentual_aumento = float(input("Informe o percentual de aumento: "))

# Cálculo do novo salário
novo_salario = salario_atual + (salario_atual * (percentual_aumento / 100))

# Exibindo o resultado
print(f"O novo salário é: R$ {novo_salario:.2f}")

#O f em f-string no Python é uma forma de formatar strings introduzida no Python 3.6. 
# Ele permite que você insira expressões dentro de chaves {} diretamente em uma string, 
# tornando o código mais legível e conciso.
