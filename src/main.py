from frota import *
import pickle

def operar(opcao : Carro):
    print(f'1- Ligar motor do {opcao.modelo}')
    print(f'2- Desligar motor do {opcao.modelo}')
    print(f'3- Acelerar do {opcao.modelo}')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        opcao.ligar()
    elif op == 2:
        opcao.desligar()
    elif op == 3:
        v = float(input(f"Informe a velocidade do {opcao.modelo}: "))
        t = float(input(f"Informe o tempo do {opcao.modelo}: "))
        opcao.acelerar(v, t)

    print('Infos atuais do carro')
    print(opcao)

if __name__ == "__main__":
    print('Cadastre o carro 1')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    nm_consumoMedio = float(input('Digite o consumo medio: '))
    nm_tanque = float(input('Digite o nivel do tanque: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, nm_tanque, nm_consumoMedio)

    print('Cadastre o carro 2')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    nm_consumoMedio = float(input('Digite o consumo medio: '))
    nm_tanque = float(input('Digite o nivel do tanque: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, nm_tanque, nm_consumoMedio)

    carros = {}
    carros[id(carro1)] = carro1
    carros[id(carro2)] = carro2

    try:
        with open('carros.pkl', 'wb') as arquivo:
            pickle.dump(carros, arquivo)
    except Exception as e:
        print(e)

    '''
    Controlando o carro até ele atingir 10000 Km
    '''

    while carro1.getOdometro() < 300 and carro2.getOdometro() < 300 and (carro1.getTanque() > 0 or carro2.getTanque() > 0):
        try:
            print('Qual carro deseja utilizar ?')

            opCarro = 0
            while opCarro not in (1, 2):
                opCarro = int(input('1 ou 2: '))

                if opCarro == 1:
                    operar(carro1)
                elif opCarro == 2:
                    operar(carro2)
                else:
                    raise Exception("Opcao invalida!!")

        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    print(carro1)
    print('Parar para trocar óleo!!!')