'''
Leia o nome e media de um aluno, guardando tambem a situacao em um dicionario.
No Final mostre a estrutura na tela
'''

boletim = dict()
situacao = dict()

while True:
    boletim['Aluno'] = str(input('Digite o nome do aluno: '))
    boletim['Média'] = str(input('Digite a média do aluno: '))
    situacao = boletim.copy()

