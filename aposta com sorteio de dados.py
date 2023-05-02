from random import randint

def definir_saldo():
    saldo = int(input('Digite a quantia que irá colocar:'))
    return saldo

def conferindo_valor():
    saldo = definir_saldo()
    if saldo <= 0:
        definir_saldo()
    return saldo

def explicando_o_jogo():
    print('EXPLICANDO O JOGO\n')
    print('Vamos sortear 2 dados e soma-los, se der 7 ou 2 voce ganha o dobro do que aposto')
    print('Se der 6, voce perde o que aposto')
    print('Se der 10, vai empatar, e voce não perde e nem ganha nada')
    print('Se nao der nenhum desses resultado, vc tera oportunidade de tentar novamente\n')

saldo = conferindo_valor()
vitoria = []
derrota = []

for aposta in range(0,1000):
    #sortei dos dados
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    #somando os dados
    soma_dos_dados = dado1 + dado2

    #explicando o jogo
    explicando_o_jogo()
    
    somas_das_vitoria = sum(vitoria)
    somas_das_derrotas = sum(derrota)

    fim_do_jogo_saldo_total = saldo + (somas_das_vitoria + somas_das_derrotas)

    print(f'Esse é seu saldo: R${fim_do_jogo_saldo_total}\n')

    valor_da_aposta = int(input('Digite o valor que ira apostar: \n'))

    if valor_da_aposta <= fim_do_jogo_saldo_total:

        if soma_dos_dados == 7 or soma_dos_dados == 2 :
            print(f'Parabens!! Voce ganhou, o resultado do dado foi {soma_dos_dados}')
            novo_saldo_vitoria = (valor_da_aposta * 2) - valor_da_aposta 
            vitoria.append(novo_saldo_vitoria)

            tentar_novamente_vitoria = int(input('Se quiser tentar novamente digite 1 caso \nSe nao quiser tentar novamente digite 2: '))
            if tentar_novamente_vitoria == 1 and fim_do_jogo_saldo_total>0:
                continue
            else:
                break

        elif soma_dos_dados == 6 or soma_dos_dados == 9 or soma_dos_dados == 5:
            print(f'Que pena, voce perdeu, o resultado do dado foi: {soma_dos_dados}')
            novo_saldo_derrota = 0 - valor_da_aposta  
            derrota.append(novo_saldo_derrota)

            tentar_novamente_derrota = int(input('Se quiser tentar novamente digite 1 caso \nSe nao quiser tentar novamente digite 2: '))
            if tentar_novamente_derrota == 1 and fim_do_jogo_saldo_total>0:
                continue
            else:
                break

        elif soma_dos_dados == 10:
            print(f'Empatou o resultado do dado foi: {soma_dos_dados}') 

            tentar_novamente_empate = int(input('Se quiser tentar novamente digite 1 caso \nSe nao quiser tentar novamente digite 2: '))
            if tentar_novamente_empate == 1 and fim_do_jogo_saldo_total>0:
                continue
            else:
                break

        else:
            print(f'Quer tentar denovo? O resultado do dado foi: {soma_dos_dados}')

            tentar_novamente = int(input('Se quiser tentar novamente digite 1 caso \nSe nao quiser tentar novamente digite 2: '))

            if tentar_novamente == 1 and fim_do_jogo_saldo_total>0:
                continue
            else:
                break
    else:
        print(f'O valor da aposta é maior que o saldo. Esse é seu saldo: {saldo}')

somas_das_vitoria = sum(vitoria)
somas_das_derrotas = sum(derrota)
fim_do_jogo_saldo_total = saldo + (somas_das_vitoria + somas_das_derrotas)

print(f'ESSE FOI O SEU SALDO COM O ENCERRAMENTO DO JOGO: R${fim_do_jogo_saldo_total}')