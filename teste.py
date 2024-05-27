import random
#  print("R$ {}".format(1.59))

# Para trabalhar com formatação:
# para informar que o número que eu estou passando é do tipo float {:f}
# print("R$ {:f}".format(1.59))

# definir as regras de quantos números deveriam vir antes e/ou depois da vírgula
# Depois do ponto eu quero 2 casas {:.2f}
# print("R$ {:.2f}".format(1.59))

#Para preencher com zeros a frente da vírgula, no caso quero que meu número tenha 7 caracteres, a vírgula também conta
# print("R$ {:07.2f}".format(1.59))

#se fosse fazer a formatação para números inteiros, ao invés de I de inteiro, é usado d
# print("R$ {:07d}".format(1))

#Formatação de datas:
# print("Data {:02d}/{:02d}".format(9,4))

# recurso para realizar a interpolação de strings. Dessa forma o Python consegue, em tempo de execução, captar a expressão que está entre chaves ({ }) e avaliá-la.
# nome = 'Karla'
# print(f'meu nome é {nome}')

numero_random = random.random() * 100
# print(int(numero_random)) #função int corta os demais números a partir do zero
print(round(numero_random)) # round arredonda o valor
