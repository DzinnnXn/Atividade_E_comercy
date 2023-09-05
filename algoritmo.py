import os

from classes import *
def main():
    s = 0
    while s == 0:
        acessador = 0
        print("LOJA DE ELETRÔNICOS")
        print("1 - Login")
        print("2 - Cadastrar")
        print("3 - Produtos")
        print("4 - Sair")
        menu = int(input("Selecione: "))
        match menu:
            case 1:
                if acessador == 1:
                    pass

                else:
                    print("Cadastro ainda não feito")
                    os.system("pause")

            case 2:
                print("CADASTRO")
                nome = input("Digite seu nome: ")
                cpf = int(input("Digite seu cpf:"))
               
            case 3:
                print("PRODUTOS")
        
            case 4:
                break

            case _:
                print("Opção inválida")
                os.system("pause")