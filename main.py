automato = open("automato.txt", "r")

estados = automato.readline().split()

alfabeto = automato.readline().split()

estadoInicial = automato.readline().split()

estadosFinais = automato.readline().split()

trilha = []

for i in range(len(estados)):
    trilhaAutomato = automato.readline().split()
    if len(trilhaAutomato) == len(alfabeto)+1:
        trilha.append(trilhaAutomato)
    else:
        raise Exception("Automato inválido")


entrada = open("entrada.txt", "r")

entradas = []
linha = entrada.readline().rstrip()
while len(linha) > 0:
    entradas.append(linha)
    linha = entrada.readline().rstrip()
print("Entradas:")
for i in entradas:
    print(i)

saida = open("saida.txt", "w+")

def checkAceita(atualFinal):
    aceita = False
    for final in estadosFinais:
        if final == atualFinal:
            aceita = True
    return aceita

def findAtual(entrada, atual, aceito):

    for i in range(len(entrada)):

        lastAtual = atual
        char = entrada[i]

        # achar o prox atual.
        coluna = 0
        linha = 0
        for x in range(len(estados)):
            if atual == str(estados[x]):
                coluna = x

        if char == 'E':
            linha = len(alfabeto)
            restoInt = -(len(entrada) - i - 1)
            if restoInt == 0:
                break
            restoentrada = entrada[restoInt:]
            copiaResposta, aceito = findAtual(restoentrada, trilha[coluna][linha], aceito)
            copiaAceita = checkAceita(copiaResposta)
            if copiaAceita == True:
                aceito = True
        else:
            for x in range(len(alfabeto)):
                if char == alfabeto[x]:
                    linha = x

        atual = trilha[coluna][linha]

        if atual == '0':
            atual = lastAtual
            break

        if "," in atual:
            copias = atual.split(',')
            for copia in copias:
                restoInt = -(len(entrada)-i-1)
                if restoInt == 0:
                    break
                restoentrada = entrada[restoInt:]
                copiaResposta, aceito = findAtual(restoentrada, copia, aceito)
                copiaAceita = checkAceita(copiaResposta)
                if copiaAceita == True:
                    aceito = True

        if aceito == True:
            return atual, aceito

    return atual,aceito



for entradaLinha in entradas:
    atual = estadoInicial[0]

    atualFinal, aceito = findAtual(entradaLinha, atual, False)

    aceita = checkAceita(atualFinal)

    if aceita == True or aceito == True:
        saida.write("ACEITA\n")
    else:
        saida.write("NEGADO\n")

automato.close()
entrada.close()
saida.close()

