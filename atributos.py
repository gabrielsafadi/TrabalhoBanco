class conta:

        print("=*"*20)
        print('BANCO ALAGOANO - O SEU BANCO DO PEITO')
        print("=*"*20)
        print(' ')
        print(' ')
        print('Para começar, digite as informações abaixo: \n')
        saldo = 0
        #recebendo informações
        banco = input ("Banco: ")
        agencia = int(input ("Agência: "))
        titularDaConta = input ("Nome do titular da conta: ")

        print("\nOlá,", titularDaConta,"\nSeu saldo é:", saldo)

        def transf(self, valor):
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                print('Saldo insuficiente.')

        def depositar(self, valor):	
                self.saldo += valor

        def sacar(self, valor):	
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                print('Saldo insuficiente.')
                

        def menu(self):
                saldo = 0
                print('=*' * 20)
                print(f'     MENU DO BANCO ALAGOANO')
                print('=*' * 20)
                print('Opções disponíveis:')
                print('1 - Transferência')
                print('2 - Depósito')
                print('3 - Saque')
                print('4 - Sair')
                numero = input('Digite a opção desejada: ')
                # if opcao == '1':
                #     self.transf()
                
                if numero == '1':
                    transfValor = float(input('Digite o valor de transferência: '))
                    transfConta = input('Digite a conta de destino: ')
                    transfAgencia = input('Digite a agência de destino: ')
                    transfNome = input('Digite o nome do titular de destino: ')

                    self.transf(transfValor)


                elif numero == '2':
                    valor = float(input('Digite o valor de depósito: '))
                    self.depositar(valor)
                    deposito = saldo + valor
                    print("Seu saldo atual é:", deposito)

                elif numero == '3':
                    saque = float(input('Digite o valor de saque: '))
                    self.sacar(saque)


                elif numero == '4':
                    exit()  

a = conta()

while True:
    a.menu()
    
    
    
    
    
    
    
    
    
    
    # a = None
    # while a != 0:
    #     a = input("""Escolha uma das opções abaixo:
    #         0 Sair
    #         1 Depositar
    #         2 Transferir
    #         3 Sacar
    #         """)
    #     if a == 1:
    #         quanto = int(input('Valor do depósito: '))
    #         if quanto > 0:
    #             valorFinal = saldo + quanto
    #             print(valorFinal)
    #     elif a == 2:
    #         transf = input('Para continuar com a transferência, complete as informações abaixo: ')
    #         bancoTransf = input('Banco de destino: ')
    #         agenciaTransf = int(input('Agência de destino: '))
    #         valorTransf = (int(input('Valor a ser transferido: ')))
    #         if valorTransf > 0:
    #             valorAtual = saldo - quanto
    #             print(valorAtual)
    #     elif a == 3:
    #         print('sacar')
    
 

