# Ordem de Precedência contas
# 1: Parênteses (), 2: ** Potências, 3: * Mult, / Div, // Divisão inteira e % resto da Divisão
# 4: + e -

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divInte = n1 // n2
poten = n1 ** n2
print('A soma é {}, \n o produto é a divisão é {:.3f}' .format(soma, mult, div, divInte, poten), end= ' ')
print ('\n Divisão inteira {} e potência {}'.format(div, poten))

