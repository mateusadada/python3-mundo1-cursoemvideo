# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('Bem vindo ao programa de cálculo que exibe o dobro, o triplo e a raiz quadrada de um número!')

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(f'\nO dobro de {numero} vale {dobro}'
      f'\nO triplo de {numero} vale {triplo}'
      f'\nA raiz quadrada de {numero} é igual a {raiz_quadrada:.2f}')
