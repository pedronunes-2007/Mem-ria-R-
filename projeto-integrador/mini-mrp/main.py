#Nicolas D. - Menu e MPS 
def exibir_menu():
    print("\n---SISTEMA MRP(PCP)---")
    print("1. Inserir demanda (MPS)")
    print("2. Ver plano de produção")
    print("3. Executar motor de explosão")
    print ("4. Sair")

def main ():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            produto = input("Produto final: ")
            qtd = int(input("Quantidade: "))
            semana = int(input("Semana de entrega (1-8): "))
            print(f"\n Demanda de {qtd} unidades de {produto} para a semana {semana} registrada.")
        elif opcao == "4": 
            print("encerrando o programa...")
            break
        else:            print("Opção em desenvolvimento. Tente novamente mais tarde.")

if __name__ == "__main__":
    main() 

#Laura Rezende - Motor de explosão




#Nicolas G. -




#funcao restante