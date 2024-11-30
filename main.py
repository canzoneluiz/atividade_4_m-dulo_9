def main():
    print("Bem-vindo à calculadora interativa")
    while true:
        print("\nEscolha uma operção")
        print("1-soma")
        print("2-subtração")
        print("3-multiplicação")
        print("4-divisão")
        print("5-sair")

        opcao = input("digite o número da operação desejada: ")

        if opcao == '5':
            print("Encerrando a calculadora, até a próxima")
            break

        if opcao in ['1','2','3','4]
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