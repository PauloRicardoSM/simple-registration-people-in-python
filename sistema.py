from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'python.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Programa'])
    
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo do programa... Até logo!')    
        break    
    else:
        print('\033[0;31mErro! Digite uma opção válida. \033[m')
    
    sleep(1)
