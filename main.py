def main():
    print("Bem-vindo à Calculadora Interativa!")
    while True:
        print("\nEscolha uma operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        
        opcao = input("Digite o número da operação desejada: ")
        
        if opcao == '5':
            print("Encerrando a calculadora. Até a próxima!")
            break
        
        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == '1':
                    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
                elif opcao == '2':
                    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
                elif opcao == '3':
                    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
                elif opcao == '4':
                    if num2 != 0:
                        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Erro: Divisão por zero não é permitida!")
            except ValueError:
                print("Erro: Entrada inválida. Por favor, insira números válidos.")
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()
