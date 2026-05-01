#Nicolas D. - Menu e MPS 
def exibir_menu():
    print("\n" + "="*30)
    print("   SISTEMA MRP - APPLE IND.   ")
    print("="*30)
    print("1. Inserir demanda de iPhone")
    print("2. Ver plano de produção")
    print("3. Executar motor de explosão")
    print ("4. Sair")
   

def main ():
    produto = ""
    quantidade_pedida = 0
    semana_entrega = 0
    pedido_existe = False

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = input("Modelo do iPhone (Ex: iPhone 15): ")

            quantidade_pedida = int(input("Quantidade: "))
            while quantidade_pedida <= 0:
                print("Erro. Quantidade deve ser maior que 0. Tente novamente.")
                quantidade_pedida = int(input("Quantidade: "))

            semana_entrega = int(input("Semana de entrega (1-8): "))
            while semana_entrega < 1 or semana_entrega > 8:
                print("Erro. A semana de entrega deve ser entre 1 e 8. Tente novamente.")
                semana_entrega = int(input("Semana de entrega (1-8): "))
            
            pedido_existe = True
            print(f"\n Demanda de {quantidade_pedida} unidades de {produto} para a semana {semana_entrega} registrada.")      
        elif opcao == "2":
            if pedido_existe:
                print("\n--- RESUMO DO PLANO MESTRE ---")
                print(f"produto: {produto}")
                print(f"Volume: {quantidade_pedida} unidades")
                print(f"Prazo:sSemana {semana_entrega}")
            else:
                print("\nNenhuma demanda registrada. Por favor, insira uma demanda primeiro.")
        elif opcao == "3":
            print("\nExecutando motor de explosão...")
        elif opcao == "4":
            print("encerrando o programa...")
            break
        else:
            print("Opção em desenvolvimento. Tente novamente mais tarde.")

if __name__ == "__main__":
    main() 

#Laura Rezende - Motor de explosão




#Nicolas G. -




#funcao restante