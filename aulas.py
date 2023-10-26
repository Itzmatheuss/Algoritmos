print("Hello World")
import math
import random
def excesso():
    p = float(input("Digite quantos quilos foram trazidos:"))
    excesso = p -50
    if excesso == 0 or excesso < 0:
        print("Não sera paga multa") 
    if excesso > 0:
        multa = excesso*4
        print(f"Seu excesso de peso foi de {excesso}kg e sua multa sera de R$:{multa}")

def tinta():
    # Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
    #Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    # Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    # comprar apenas latas de 18 litros;
    # comprar apenas galões de 3,6 litros;
    # misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 
    m = float(input("Informe o tamanho em m² do local a ser pintado:"))
    l = 18
    g = 3.6

    cobertura = 1/6
    pl = 80
    pg = 25

    qntTinta = (m*cobertura)*1.1
    print(qntTinta)
    qLatas = math.ceil(qntTinta/l)
    qGalao = math.ceil(qntTinta/g)
    print(qGalao)

    precoLata = qLatas*pl
    precoGalao = qGalao*pg
    print(f"O preço para pintar {m}m² com apenas latas sera de {precoLata} reais")
    print(f"O preço para pintar {m}m² com apenas galões sera de {precoGalao} reais")

    comb_latas = math.floor(qntTinta/l)
    resto = math.ceil(qntTinta -(comb_latas*l))
    qntGalao = math.ceil(resto /g)
    ptotal = (comb_latas*pl) + (qntGalao*pg)
    print(f"Usando a combinação de {comb_latas} latas e {qntGalao} galões com um preço de {ptotal} reais")


def cleusa():
    ano = int(input("Digite seu ano de nascimento:"))
    anoatual = int(input("Digite o ano em que estamos:"))
    velinha = anoatual-ano
    print("A qnt de velas nescessarias sera:",velinha)
    
    real = float(input("Quantos reais você possui:"))
    dolar = real/5.06
    print(f"Você teria {dolar} dolares ")

    temp = float(input("Qual a temperatura atual:"))

    c = (temp -32)/1.8
    print(c)
    p = float(input("QUal o valor do produto"))
    imposto = p*0.2
    print(imposto)
    valor = float(input("Qual o valor do emprestimo:"))
    juros = valor*1.2
    parcelas = int(input("Quantas parcelas ?"))
    vp = juros/parcelas
    print(f"O valor de cada parcela sera de {vp}, ao todo sera pago um total de {juros}")



def imc():
    peso = float(input("Qual o seu peso atual ?"))
    altura = float(input("Qual a sua altura ?"))
    imc = peso/(altura**2)
    print(imc)
    if imc <17:
        print("Muito abaixo do peso")
    elif imc>17 and imc <18.5:
        print("Abaixo do peso")
    elif imc>=18.5 and imc<25:
        print("Parabens voce esta no seu peso ideal")
    elif imc >=25 and imc <30:
        print("Você com sobrepeso")
    elif imc >=40:
        print("obesidade morbida")

def aluno():
    n1 = float(input("Primeira nota:"))
    n2 = float(input("Segunda nota:"))
    media = (n1+n2)/2
    if media>=9:
        print("A")
    elif media <9 and media >=8:
        print("B")
    elif media >= 7 and media <8:
        print("C")
    elif media >= 6 and media <7:
        print("D")
    elif media >=5 and media <6:
        print("E")
    else:
        print("F")
    print(media)

def repeticao():
   
    f = int(input("Digite até qual elemento calcular fibonacci:"))
    cont = 0
    fib=[]
    for i in range(f):
        if i==0:
            fib.append(i)
        elif i ==1:
            fib.append(i)
        elif i ==2:
            fib.append(i-1)
        elif i>=3:
            cont = fib[i-1] + fib[i-2]
            fib.append(cont)
    print(fib)


    # soma = 0
    # cont = 0
    # nulo = 0
    # par =0
    # for i in range(5):
    #     v = float(input(f"Digite o {i+1}° valor:"))
    #     soma += v
    #     dfive = v%5
    #     dpar = v%2
    #     if dfive ==0:
    #         cont += 1
        
    #     if v ==0:
    #         nulo+=1

    #     if dpar == 0:
    #         par += v

    # media = soma/5
    # print(f"A soma entre os valores é: {soma}")
    # print(f"A media entre os valores é: {media}")
    # print(f"Valores divisiveis por 5 : {cont}")
    # print(f"Valores nulos: {nulo}")
    # print(f"A soma entre os valores pares é: {par}")


    # cont = 0
    # soma = 0
    # for i in range(6):
    #     a = int(input("Digite um valor:"))
    #     if 0 <= a <=10:
    #         cont +=1
    #         impar = a%2
    #     if impar ==1:
    #         soma = a + soma
    # print(f"Ao todo foram inseridos {cont} valores entre 0 e 10.")
    # print(f"A soma dos valores impares inseridos é igual a: {soma}.")


    # homem = {"idade":0,"cabelo":""}
    # mulher ={"idade":0,"cabelo":""}
    # hlist = []
    # mlist = []
    # while True:
    #     sexo = input("Qual o sexo ?  [M/F]" ).upper()
    #     if  sexo == "M":
    #         idade = int(input("Qual a idade ?"))
    #         if idade >=18:
    #             homem["idade"]=idade
    #         print("Escolha a cor do cabelo")
    #         print("[1] Preto")
    #         print("[2] Castanho")
    #         print("[3] Loiro")
    #         print("[4] Ruivo")
    #         cabelo = int(input("Digite o valor da cor do cabelo:"))
    #         if cabelo==2:
    #             homem["cabelo"] = "castanho"
    #         if idade >=18 and cabelo ==2:
    #             hlist.append(homem)

    #     elif  sexo == "F":
    #         idade = int(input("Qual a idade ?"))
    #         if idade >=18:
    #             mulher["idade"]=idade
    #         print("Escolha a cor do cabelo")
    #         print("[1] Preto")
    #         print("[2] Castanho")
    #         print("[3] Loiro")
    #         print("[4] Ruivo")
    #         cabelo = int(input("Digite o valor da cor do cabelo:"))
    #         if cabelo==3:
    #             mulher["cabelo"] = "loiro"
    #         if (idade >=25 and idade <=30) and cabelo ==3:
    #             mlist.append(mulher)
            
    #     print("Quer continuar ?  [S/N]")
    #     answer = input().upper()
    #     if answer == "N":
    #         print(f"Total de homens com mais de 18 anos e cabelos castanhos: {len(mlist)} ")
    #         print(f"Total de mulheres entre 25 e 30 anos e cabelos loiros: {len(mlist)} ")
    #         break
        


    # while True:
    #     print("MENU de contagem")
    #     print("[1] De 1 a 10")
    #     print("[2] De 10 a 1")
    #     print("[3] Sair")
    #     a = int(input("Digite um numero:"))
    #     if a == 1:
    #         cont = 0
    #         for i in range(10):
    #             cont+= 1
    #             print(cont)
    #     elif a == 2:
    #         cont =11
    #         for i in range(10):
    #             cont-= 1
    #             print(cont)
    #     else:
    #         print("F I M")
    #         break
    #Verifica se o numero digitado é primo

    # cont = 1
    # valor = int(input("Digite um numero:"))
    # for i in range(valor):
    #     result = valor % cont
    #     if result ==0:
    #         cont+=1
    #     elif cont ==2:
    #         print(f"O valor {valor} é primo")
    #     else:
    #         print(f"O valor {valor} não é primo")
    

    # resp = "S"
    
    # while resp == "S":
    #     fat = int(input("Qual o valor:"))
    #     cont = fat
    #     resultado=0
    #     for i in range(fat):
    #         fatorial = fat * cont
    #         resultado = fatorial+resultado
    #         cont-=1
    #     print(f"O fatorial de {fat} é ={resultado}")
    #     resp =input("Quer continuar:?")


    # cont =0
    # neg = 0
    # for i in range(5):
    #     n = float(input("Digite um valor:"))
    #     if n <0:
    #         neg+= 1
    #     else:
    #         cont +=1
    # print(f"Foram digitados {neg} valores negativos")

    # bestA = {"nome":"","nota":0}
    # alunos = int(input("Quantos alunos existem na turma:"))
    # for i in range(alunos):
    #     print(f"Aluno {i+1}")
    #     nome = input("Nome do Aluno:")
    #     nota = float(input(f"Digite a nota de {nome}:"))
    #     if nota > bestA["nota"]:
    #         bestA["nome"]=nome
    #         bestA["nota"] =nota
    # print(f"Nome: {bestA['nome']} foi o melhor aluno com a nota {bestA['nota']}")


    # incio = int(input("Digite o valor inicial:"))
    # fim = int(input("Digite o valor final:"))
    
    # if incio>fim:    
    #     for i in range(incio):
    #         cont = incio -i
    #         print(cont,"..")
    # else:
    #     for i in range(fim):
    #         cont = fim - i
    #         print(cont,"..")
    # while True:
    #     nota = float(input("Digite um valor entre 0 e 10:"))
    #     if nota>10 or nota <0:
    #         print("Digite um valor válido!!!")
    #     else:
    #         print("Nota valida",nota)
    #         break


    # while True:
    #     user = input("Digite seu usuario")
    #     senha = input("Digite sua senha")
    #     if user == senha:
    #         print("Usuario e Senha iguais digite uma nova senha e novo usuario")
    #     else:
    #         break

def fibo(a):
    cont = 0
    fib=[]
    for i in range(a):
        if i==0:
            fib.append(i)
        elif i ==1:
            fib.append(i)
        elif i ==2:
            fib.append(i-1)
        elif i>=3:
            cont = fib[i-1] + fib[i-2]
            fib.append(cont)
    print(fib)

def funcao():
    f = int(input("Digite até qual elemento calcular fibonacci:"))
    fibo(f)
    x = 5
    y=3
    funcSoma(x,y)
def parImpar(x):
    calc = x%2
    if calc ==0:
        return "É par"
    else:
       return "É impar"
    

    # x = float(input("Insira um valor:"))   
    # res =parImpar(x)
    # print(res)    

def funcSoma(a,b):
    return a+b

def calcular():
    v1= float(input("Insira um valor:"))
    v2= float(input("Insira um valor:"))
    res =funcSoma(v1,v2)
    if res >=3:
        print(f"A soma dos valores é:{res}")

def calFat(a):
    fat = math.factorial(a)
    return fat
    # v = int(input("Insira o valor do calculo fatorial"))
    # res = calFat(v)
    # print(f"O valor ! de {v} é igual a {res}")

def internalFunc():
    n = str(input("Digite seu nome:")).upper()
    primeiro  = n[-1]
    posicao = n.find('X')
    print(f"Total de letras do seu nome: {len(n)}") 
    print(f"Nome em maiuscula: {n.upper()}")
    print(f"A ultima letra do meu nome é {primeiro}")
    print(f"A letra X foi encontrada na posição: {posicao}")

    n_invertido = n[::-1]
    print(n_invertido)


def salto():
    # Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo: 

    atleta = []
    notas = []
    nome = input("Insira o nome do atleta:")
    atleta.append(nome)
    for i in range(7): 
        nota = float(input(f"Digite a nota {i+1} do {nome}:"))
        notas.append(nota)
    maior = max(notas)
    rmaior = notas.remove(maior)
    menor = min(notas)
    rmenor = notas.remove(menor)
    media = (sum(notas)/len(notas))
    print(media)
    

def vetor():
    
    
    a
    
    #Reserva lugar

    # cadeiras = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10"]
    # reservados = []
    # while True:
    #     print(cadeiras)
    #     print("-"*35)
    #     res = input("Reservar cadeira:").upper()
    #     for i in range(len(cadeiras)):
    #         if res == cadeiras[i]:
    #             reservados.append(cadeiras[i])
    #             cadeiras[i]= "--"
    #             print("Cadeira Reservada")
    #             break
    #         elif res in reservados:
    #             print("Erro: Lugar Ocupado")
    #             break
    #     print("-"*35)
    #     endl = input("Quer reservar mais um lugar ? [S/N]").upper()
    #     if endl == "N":
    #         break
    
    #Tabela jogos
    # times=[]

    # qntimes = int(input("Digite quantos times jogarão o campeonato:"))
    
    # for i in range(qntimes):
    #     time = input(f"Nome do {i+1} time:")
    #     times.append(time)

    # for i in range(len(times)):
    #     for j in range(i+1, len(times)):
    #         if i !=j:
    #             print(f"{times[i]} [] x [] {times[j]}")
    #             print(f"{times[j]} [] x [] {times[i]}")

    #comparação de vetores
    # gabarito=[]
    # alunos=[]
    # notas=[]
    
    # cont = 0 
    # questoes = int(input("Quantas questoes sao:"))
    # for i in range(questoes):
    #     print("Passo 1 - Cadastro Gabarito")
    #     print("-"*35)
    #     q = input(f"Insira a alternativa correta para a Questão {i+1}:").upper()
    #     gabarito.append(q)
    # qalunos = int(input("Quantos alunos serao inseridos:"))

    # for i in range(qalunos):
    #     cont = 0
    #     print("-"*35)
    #     nome = input(f"Nome do {i+1}° Aluno:")
    #     alunos.append(nome)
    #     print("-"*35)
    #     for i in range(len(gabarito)):
    #         print("-"*35)
    #         resAluno = input(f"Questão {i+1}:").upper()
    #         if resAluno == gabarito[i]:
    #             cont += 2
    #         else:
    #             cont+=0
        
    #     notas.append(cont)
    #     media = sum(notas)/len(notas)
    
    # print("-"*35)    
    # print("Notas finais")
    # print("-"*35)
    # for i in range(len(alunos)):
    #     print(f"{alunos[i]}   {notas[i]}")
    #     print("-"*35)
    # print(f"Media da turma {media}")


    #ordenando valores no vetor

    # valores =[]
    # for i in range(10):
    #     v = float(input("Digite um valor:"))
    #     valores.append(v)
    # print("Antes da ordenação",valores)
    # print("-"*35)
    # for i in range(len(valores)-1):
    #     for j in range(i+1,len(valores)):
    #         if valores[i]>valores[j]:
    #             aux = valores[i]
    #             valores[i]=valores[j]
    #             valores[j] = aux

    # print("Pós ordenação",valores)


    # nomes=[]
    # for i in range(2):
    #     n = input("Qual o seu nome:").upper()
    #     primeira_letra = n.find("C")
    #     if primeira_letra == 0:
    #         nomes.append(n)
    # print(nomes)

    # nomes=[]
    # nota1=[]
    # nota2=[]
    # media=[]
    # cont =0
    # a = int(input("Quantos alunos serao inseridos ?"))
    # for i in range(a):
    #     nome = input(f"Nome do aluno {i+1}:")
    #     n1 = float(input(f"Primeira Nota do Aluno {i+1}:"))
    #     n2 = float(input(f"Segunda nota do aluno {i+1}:"))
    #     nota1.append(n1)
    #     nota2.append(n2)
    #     nomes.append(nome)
    #     m = (n1+ n2)/2
    #     media.append(m)
    # print("-"*35)
    # for i in range(len(nomes)):
    #     print(f"{nomes[i]} com media :{media[i]}")
    #     mt = sum(media)/len(media)
    #     if media[i]>=mt:
    #         cont+=1
    # print(f"temos {cont} alunos acima da media da turma: {mt}")
    

    # n= [0,0,0,0,0,0,0]
    # index = []
    # cont = 0
    # for i in range(len(n)):
    #     a = float(input(f"Digite o {i+1}° valor:"))
    #     n[i]=a
    #     par = a%2
    #     if par ==0:
    #         index.append([i])
    #         cont+=1
    # print(n)    
    # print(f"Temos {cont} numeros pares nesta lista na posiçaõ {index}")

def matriz():
    # jogo da velha

    matriz=[[1,2,3],
            [4,5,6],
            [7,8,9]]
    jogadas = []

    def imprimirMatriz():
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                print(f"[{matriz[i][j]:2}]",end='')
            print()
        print('-'*35)
    
    def verificaVitoria(jogador):
        for i in range(3):
            if all(matriz[i][j] == jogador for j in range(3)):
                return True
            if all(matriz[j][i] == jogador for j in range(3)):
                return True
        if all(matriz[i][i] == jogador for i in range(3)) or all(matriz[i][2-i] == jogador for i in range(3)):
            return True
        else:
            return False    
            
                

    while True:
        imprimirMatriz()
        res = int(input("Vai jogar [X] em qual posição ?  [1-9]"))

        while res <1 or res >9 or res in jogadas:
            print("Movimento Invalido !")
            res = int(input("Vai jogar [X] em qual posição ?  [1-9]"))

        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if res == matriz[i][j]:
                    matriz[i][j] = "X"
                    jogadas.append(res)
                    break
      

        imprimirMatriz()
        
        if verificaVitoria("X") == True:
            print("X venceu")
            break

        if len(jogadas) ==9:
            print("Empate")
            break  

        bola = int(input("Vai jogar [O] em qual posição ? [1-9]"))
       
        while bola <1 and bola >9 or bola in jogadas:
            print("Movimento invalido !")
            bola = int(input("Vai jogar [O] em qual posição ? [1-9]"))       
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if bola == matriz[i][j]:
                    matriz[i][j] = "O"
                    jogadas.append(bola)
                    break
      
            
        
        if verificaVitoria("O") == True:
            print("O venceu")
            break 

        
        
    #mostra matriz

    # matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    # for i in range(len(matriz)):
    #     for j in range(len(matriz)):
    #         matriz[i][j] = random.randint(1,100)

    # while True:
    #     print("Menu de Opções")
    #     print("-"*35)

    #     print("[1] Mostrar Matriz")
    #     print("[2] Diagonal Principal")
    #     print("[3] Triangulo Superior")
    #     print("[4] Triangulo Inferior")
    #     print("[5] Sair")
    #     print("-"*35)
    #     res = int(input("Digite a opção desejada:"))
    #     if res ==1:
    #         for i in range(len(matriz)):
    #             for j in range(len(matriz)):
    #                 print(f"[{matriz[i][j]:^5}]",end='')
    #             print()
    #     if res ==2:
    #         for i in range(len(matriz)):
    #             for j in range(len(matriz)):
    #                 if i ==j:
    #                     print(f"[{matriz[i][j]:2}]")
                    
                    
    #     if res == 3:
    #         for i in range(len(matriz)):
    #             for j in range(len(matriz)):
    #                 if i < j :
    #                     print(f"[{matriz[i][j]}]")

    #     if res ==4:
    #         for i in range(len(matriz)):
    #             for j in range(len(matriz)):
    #                 if i > j :
    #                     print(f"[{matriz[i][j]}]")
    #     if res == 5:
    #         break

    #matriz 4ordem

    # matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0,],[0,0,0,0]]
    # soma =0
    # maior =0
    # prod=1
    # for i in range(len(matriz)):
    #     for j in range(len(matriz)):
    #         matriz[i][j] = random.randint(1,10)
    #         if i ==j:
    #             soma =matriz[i][j] +soma
    
    # for i in range(len(matriz)):
    #     for j in range(len(matriz)):
    #         print(f"[{matriz[i][j]:^5}]",end='')
    #     print()

    # for i in range(len(matriz)):
    #     prod = prod * matriz[1][i]

    # for i in range(len(matriz)):
    #     if matriz[i][2] > maior:
    #         maior = matriz[i][2]    
    # print(f"Soma da diagonal principal é {soma}")
    # print(f"O produto da segunda linha é {prod}")
    # print(f"O maior numero da 3 coluna é {maior}")


    #Diagonal principal
    # mId = [[0,0,0],[0,0,0],[0,0,0]]

    # for i in range(len(mId)):
    #     for j in range(len(mId)):
    #         if i ==j:
    #             mId[i][j]=1
    #         else:
    #             mId[i][j] =0
    
    # for i in range(len(mId)):
    #     for j in range(len(mId)):
    #         print(f"[{mId[i][j]:4}]",end='')
    #     print()


    # matriz =[[0,0,0],[0,0,0],[0,0,0]]
    # cont =0
    # for i in range(3):
    #     for j in range(3):
    #         matriz[i][j] = random.randint(1,100)
    #         res = matriz[i][j]%2
    #         if res ==0:
    #             cont+=1
    # print(f"Existem {cont} numeros pares")
    # for i in range(3):
    #     for j in range(3):
    #         print(f"[{matriz[i][j]:^5}]",end='')
    #     print()

matriz()