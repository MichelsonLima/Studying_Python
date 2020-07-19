from sys import exit
from colorama import Fore
import os
clear = lambda: os.system('cls')
from time import sleep
class Calculadora():
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def divisao(self):
        return self.a / self.b

    def multiplica(self):
        return self.a * self.b

def main():
      
    choose = 0
    while choose != 5:
        print(Fore.MAGENTA + "Calculadora Premium")
        print(Fore.CYAN + "Digite o primeiro número:\n")
        num1 = float(input(Fore.GREEN+">> "))

        print(Fore.CYAN+"Digite o segundo número:\n")
        num2 = float(input(Fore.GREEN + ">>"))

        calcu = Calculadora(num1, num2)
        print(Fore.CYAN+"Escolha a operação:")
        print(Fore.MAGENTA+ " (1) Adição \n (2) Subtração \n (3) Multiplicação \n (4) Divisão\n (5) Sair")
        choose = int(input(">>"))
        if choose == 1:
            print(Fore.YELLOW + "O resultado da soma é: "+ str(calcu.soma()))
            print(Fore.GREEN+"Deseja limpar o dashbord? \nDigite (1) Sim (2) Não ")
            x = int(input(">>"))
            if x == 1:
                clear()
            print(Fore.BLUE+"Deseja encerrar sua sessão?\n(1) Sim    (2) Não")
            y = int(input(">>"))
            if y == 1:
                exit()
                
        elif choose == 2:
            print(Fore.YELLOW + "O resultado da subtração é: "+str(calcu.subtracao()))
            print(Fore.GREEN+"Deseja limpar o dashbord? \nDigite (1) Sim (2) Não ")
            x = int(input(">>"))
            if x == 1:
                clear()
            print(Fore.BLUE+"Deseja encerrar sua sessão?\n(1) Sim    (2) Não")
            y = int(input(">>"))
            if y == 1:
                exit()    
                
        elif choose == 3:
            print(Fore.YELLOW + "O resultado da multiplicação é: "+str(calcu.multiplica()))
            print(Fore.GREEN+"Deseja limpar o dashbord? \nDigite (1) Sim (2) Não ")
            x = int(input(">>"))
            if x == 1:
                clear()
                
            print(Fore.BLUE+"Deseja encerrar sua sessão?\n(1) Sim    (2) Não")
            y = int(input(">>"))
            if y == 1:
                exit()    
                
        elif choose == 4:   
            print(Fore.YELLOW + "O resultado da divisão é: "+ str(calcu.divisao()))
            print(Fore.GREEN+"Deseja limpar o dashbord? \nDigite (1) Sim (2) Não ")
            x = int(input(">>"))
            if x == 1:
                clear()
                
            print(Fore.BLUE+"Deseja encerrar sua sessão?\n(1) Sim    (2) Não")
            y = int(input(">>"))
            if y == 1:
                exit()    

        elif choose ==5:
            exit()
            
        else:
            print(Fore.RED+"Número de operação inválido. Tente novamente.")
            sleep(3)
            clear()
        
      



if __name__ == '__main__':
    main()
