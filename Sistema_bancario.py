menu = '''
          MENU:
          
          [d] - Depositar
          [s] - Sacar
          [e] - Extrato
          [S] - Saldo
          [q] - Sair
        
'''

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
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
            lista_de_movimentacoes.append(f"Depósito de R$ {valor_deposito}")
            
            
                    
    elif opcao == "s":
        print("Saque")
        
        valor_saque = float(input("Informe o valor do saque:"))
        saques = numero_saques >= LIMITE_SAQUES
                
        if valor_saque > 500:
                print("Não é possível sacar o dinheiro, limite de R$ 500.00")
                
        elif valor_saque > saldo:
                    print("Valor do saque superior ao saldo em conta.")
                    
        elif saques:
                print("Limite de saques diários atingido.")
                
        else:
            saldo = (saldo - valor_saque)
            print(f"Valor do saque: R$ {valor_saque}")
            numero_saques = numero_saques + 1
            lista_de_movimentacoes.append(f"Saque de R$ {valor_saque}")
            
        
                                                               
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