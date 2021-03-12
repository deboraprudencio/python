#OPERADORES BÁSICOS

    1 + 2       #soma 
    3 - 4       #subtração
    5 * 6       #multiplicação
    7 / 8       #divisão
    35 // 6     #divisão inteira (resto é ignorado)
    35 % 6      #resto da divisão inteira
    2 ** 3      #exponenciação


#CONVERSÃO DE TIPOS

    int()       #transforma o valor ou variável em integer (integral)
    float()     #transforma em float (número quebrado)
    str()       #transforma em "string" (série de caracteres)


#COMANDOS BÁSICOS

    x = 17      #guarda o valor na variável
    print()     #apresenta ao usuário o que estiver entre () (entre " " é apresentado como string)
    input()     #solicita ao usuário algum valor (entre () e " " pode-se escrever uma msg ao usuário)
    len()       #produz o tamanho (em caracteres) de um string
    import math #importa determinado grupo de comandos ausentes do básico


#FORMATAÇÃO DO PRINT

    print("blábláblá {} bláblá {}" .format(x, y))   #substitui {} pelas valores solicitadas na ordem que aparecem
    print("blábláblá %d bláblá %d" %(x, y))         #substitui %d pelos valores solicitados transformando em integers
    print("blábláblá %10.2f bláblá %10.2f" %(x, y)) #substitui transformando em float e definindo 2 casas depois do ponto em um campo de 10 (sem esses elementos, apresenta todas as casas possíveis)
    print("blabláblá %10.2s bláblá %10.2s" %(x, y)) #substitui transformando em string e reduzindo a 2 caracteres em um campo de 10


#OPERADORES BOOLEANOS

    3+2 == 5    #igual
    3+2 != 6    #diferente
    6 > 5       #maior
    6 < 7       #menor
    x >= 6      #maior ou igual
    x <= 8      #menor ou igual

    True        #denota que o solicitado é verdade (pode ser guardado em uma variável)
    False       #denota que o solicitado é falso (pode ser guardade em uma variável)

condição1 and condição2 #denota que ambas as condições precisam ser satisfeitas para que seja verdadeiro
condição1 or condição2  #denota que apenas uma das condições precisa ser satisfeita para que seja verdadeiro
    not                 #inverte a condição, valor ou variável

if condição:    #estabelece uma condição para a execução de determinado grupo de comandos
    comando1    #comando a ser executado caso a condição seja satisfeita
else:           #o que deve ser executado caso a condição não seja satisfeita
    comando2    #identação é o que define cada grupo de comandos/

while condição: #estabelece a repetição de um comando enquanto determinada condição for satisfeita
    comando1
comando 2       #assim que a condição deixar de ser satisfeita o programa segue sua execução para a linha de baixo


#MATH

    math.sqrt() #dá a raiz quadrada do valor
