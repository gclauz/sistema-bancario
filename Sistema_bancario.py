menu = '''
          MENU:
          
          [d] - Depositar
          [r] - Retirar
          [e] - Extrato
          [s] - Saldo
          [q] - Sair
        
'''

saldo = 0
limite = 500
numero_retiradas = 0
LIMITE_RETIRADAS = 3
lista_de_movimentacoes = []

while True:
    
    opcao = input(f"{menu} Informe uma opção: ")
    
    if opcao == "d":
        print("Deposito")
        
        valor_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_deposito < 0:
            print("Valor inválido")
        else: 
            saldo = (saldo + valor_deposito)
            print("Depósito feito com sucesso.")
            lista_de_movimentacoes.insert(0,f"Depósito de R$ {valor_deposito}")
            
            
                    
    elif opcao == "r":
        print("Retirar")
        
        valor_retirada = float(input("Informe o valor da retirada:"))
        retiradas = numero_retiradas >= LIMITE_RETIRADAS
                
        if valor_retirada > 500:
                print("Não é possível retirar o dinheiro, limite de R$ 500.00")
                
        elif valor_retirada > saldo:
                    print("Valor da retirada superior ao saldo em conta.")
                    
        elif retiradas:
                print("Limite de retiradas diárias atingido.")
                
        else:
            saldo = (saldo - valor_retirada)
            print(f"Valor da retirada: R$ {valor_retirada}")
            numero_retiradas = numero_retiradas + 1
            lista_de_movimentacoes.insert(0,f"Retirada de R$ {valor_retirada}")
            
        
                                                               
    elif opcao == "e":
        print("Extrato")
        
        print(lista_de_movimentacoes)
        
    
    elif opcao == "S":
        print("Saldo")
        
        print(f"R$ {saldo}")
        
    elif opcao == "q":
        print("O banco agradece pela parceria")
        print("Volte sempre!")
        break      
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
