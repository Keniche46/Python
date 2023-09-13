import random 
import time
  
def ganhar(user, random): 
     if user == random: 
         print(f'\nUser: {user}\nMáquina: {random}') 
         print('Empate\n')
         time.sleep(0.7)
     elif user == 'Pedra' and random == 'Tesoura': 
         print(f'\nUser: {user}\nMáquina: {random}') 
         print('Você ganhou!\n')
         time.sleep(0.7)
     elif user == 'Papel' and random == 'Pedra':
         print(f'\nUser: {user}\nMáquina: {random}')
         print('Você ganhou!\n')
         time.sleep(0.7)
     elif user == 'Tesoura' and random == 'Papel':
         print(f'\nUser: {user}\nMáquina: {random}')
         print('Você ganhou!\n')
         time.sleep(0.7)
     elif user == 'Tesoura' and random == 'Pedra':
         print(f'\nUser: {user}\nMáquina: {random}')
         print('Você perdeu!\n')
         time.sleep(0.7)
     elif user == 'Papel' and random == 'Tesoura':
         print(f'\nUser: {user}\nMáquina: {random}')
         print('Você perdeu!\n')
         time.sleep(0.7)
     elif user == 'Pedra' and random == 'Papel':
         print(f'\nUser: {user}\nMáquina: {random}')
         print('Você perdeu!\n')
         time.sleep(0.7)
def menu(): 
     print('Escolha a opcão que deseja jogar.') 
     print('[1]- Pedra') 
     print('[2]- Papel') 
     print('[3]- Tesoura') 
     print('[0]- Sair') 
  
escolhas_jogo = ['Pedra','Papel','Tesoura'] 
  
while True: 
     menu() 
     opção = int(input('Insira o número referente sua escolha: ')) 
     if opção == 0: 
         break 
     escolha_usuario = escolhas_jogo[opção - 1] 
     escolha_random = random.choice(escolhas_jogo) 
     ganhar(escolha_usuario, escolha_random)