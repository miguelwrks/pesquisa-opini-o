import os 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear()
print('--->Programa Pesquisa de Opnião <---\n')

#inicialização de variáveis 
contador = 0
excelente = 0 #inicializa com 0 e dps soma
bom = 0 #inicializa com 0 e dps soma
ruim = 0 #inicializa com 0 e dps soma na estrutura de repetição
opinião = 0 #inicializa 0 pra opiniao entrar ja no loop e dps da digitação ai vai conferir se eh 1, 2 ou 3

for contador in range(1,11): # 1 - pra começar no numero 1 e 11 pra ter a qtde de 10 voltas

    nome = str(input(f'Olá usuário {contador},digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    while opinião!=1 or opinião!=2 or opinião!=3:
        opinião = int(input('Qual a sua opinião sobre o nosso atendimento?\nDigite:\n1 para Excelente;\n2 para Bom;\n3 para Ruim.\n'))
        
        #break usado para parar o while e continuar
        match opinião: #contando a quantidade de opiniões, isso pq nao estamos usando arrays ainda
            case 1:
                excelente = excelente+1
                break
            case 2:
                bom = bom+1
                break
            case 3:
                ruim = ruim+1
                break
            case _:
                print('Opção inválida! Digite novamente!')
            
            
    clear()
    
clear()
print(f'No total tivemos:\n{excelente} opiniões como EXCELENTE;\n{ruim} opiniões como RUINS.\n\nbônus: {bom} opiniões como BOM.')
print('\nPrograma desenvolvido por: Miguel Silva Gonçalves.')
