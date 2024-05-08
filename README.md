|![banner-python](https://github.com/PauloRicardoSM/simple-registration-people-in-python/assets/135445155/4f496d18-2b64-4f46-953d-85eafa515cb0)|Simple Registration of People in Python|
|:---:|:---:|

Code made during the Python course [Python 3 - Mundo 3](https://www.cursoemvideo.com/curso/python-3-mundo-3/)
of the platform [Curso em Vídeo](https://www.cursoemvideo.com/). 

## About the System
This is a simple system that presents a menu to the user with three options: View Registered People, Register New Person, and Exit the Program. Despite its simplicity, the system utilizes modularization and Python packages, and it has capabilities for file creation and modification.

## Code Functionality
Initially, the system will verify the existence of a file designated to store individuals’ names and ages. In this instance, the file is pre-named ‘python.txt’. The code responsible for this verification is as follows:

**Main Code**
```
arq = 'python.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
```
**Function `arquivoExiste()`**
```
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
```
In summary, the `arquivoExiste()` function checks whether a file with the given name exists in the current directory. It tries to open the file in read-only mode. If the file does not exist, Python raises a FileNotFoundError, and the function returns False. If the file does exist, the function returns True after closing the file. 

**Function `criarArquivo()`**
```
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
```
This function, createFile, attempts to create a new file with the specified name. If the file already exists, it will be opened in write mode, which allows for writing to the file. If the file does not exist, the `‘wt+’` mode ensures that the file will be created. If any error occurs during this process, the function will catch the exception and print an error message. If no errors occur, it will print a message stating that the file was created successfully.

Following this verification, the core segment of the code is structured as shown below:

**Main Code**
``` 
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
```
Here’s a breakdown of the code’s functionality:
* The `while True` loop creates an infinite loop, which allows the program to continuously display the menu until the user decides to exit.
* The `menu` function displays the options to the user and returns their choice.
* Depending on the user’s response, the program will:
  * Read and display the file’s contents if the user wants to view the registered people (`readFile function`).
  * Register a new person by asking for their name and age and then saving this information (`register function`).
  * Exit the program if the user chooses to do so.
* If the user selects an option that is not available, an error message is displayed.
* The `sleep(1)` function call pauses the program for one second, which can help in making the program’s output more readable.

**Function `menu()`**
```
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c +=1
        
    print(linha())
    opc = leiaInt('\033[32mQual a sua opção: \033[m')
    
    return opc
```
The menu function displays a main menu and returns the user’s chosen option. It receives a list of menu items, displays each item with a corresponding number, and prompts the user to select an option.

**Function `lerArquivo()`**
```
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
```
The `lerArquivo()` function attempts to open a file for reading. If successful, it reads the file and displays the formatted data, presumably of registered individuals, where each line contains a name and an age separated by a semicolon.

**Function `cabecalho()`**
```
def cabecalho(txt):
    print(linha())
    print(txt.center(len(linha())))
    print(linha())
```
The `cabecalho()` function prints a formatted header to the console. It displays a line, followed by the centered text, and another line.

**Function `cadastrar()`**
```
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
```
The `cadastrar()` function attempts to open a file to append data at the end of it. If successful, it writes a new record to the file, containing the name and age of a person, separated by a semicolon.

### Other Functions
**Function `leiaInt()`**
```
def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n     
```
The `leiaInt()` function is designed to read an integer number from the user. It displays a message asking the user to enter a number and attempts to convert the input into an integer. If the conversion fails due to an invalid value (such as letters or symbols), it displays an error message and asks again. If the user interrupts the input (such as pressing Ctrl+C), it displays a different message and returns 0. If the input is a valid integer, it returns that number.

**Function `linha()`**
```
def linha(tam = 42):
    return '=' * tam
```
The `linha()` function returns a string composed of equal sign (‘=’) characters with a standard length of 42 characters, unless a different value is provided as an argument. This function is useful for creating visual separation lines in the console.

## Visualizing the System in Action
**Main Menu**

![screenshot](https://github.com/PauloRicardoSM/simple-registration-people-in-python/assets/135445155/80da24a6-9d2b-4295-9ae4-fccf8920ef92)

**Option 1**

![Captura de tela 2024-05-07 205546](https://github.com/PauloRicardoSM/simple-registration-people-in-python/assets/135445155/123a0b07-d22c-44fd-beaf-8e7b24df28f6)

**Option 2**

![Captura de tela 2024-05-07 205420](https://github.com/PauloRicardoSM/simple-registration-people-in-python/assets/135445155/84b81e74-71aa-486d-b910-1bdfa8b286e0)

**Option 3**

![Captura de tela 2024-05-07 205633](https://github.com/PauloRicardoSM/simple-registration-people-in-python/assets/135445155/73995c20-b4e3-4482-8858-69b75d3864b4)

## License
This project is licensed under the MIT license.

## Acknowledgments
I thank Professor Guanabara, from Cursos em Vídeo, for all the knowledge provided for free and of quality. I also thank you who are reading this README. Thank you for your attention and keep an eye out for new projects that I will be involved in the future. Contact me through the links below.

<div> 
  <a href = "mailto:pauloricardosm@alu.ufc.br"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="www.linkedin.com/in/paulo-ricardo-sousa" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
</div>


