# Eleccion de maquina
import random

num_rand = random.randint(1,3)
if num_rand==1:
    choice_maq = 'Piedra'
elif num_rand ==2:
    choice_maq = 'Papel'
else:
    choice_maq = 'Tijeras'

# Eleccion de Usueio
choice_text ='''

Escribe una opcion:
    Piedra
    Papel
    Tijera
'''
choice_user = input(choice_text)

# Imprime seleccion
print("Usuario elige ", choice_user)
print("Maquina elige ", choice_maq)
# Define ganador
if choice_user == choice_maq:
    print("Es un empate maistro")
else:
    if choice_user == 'Piedra' and choice_maq == 'Papel':
        print("Gana Maquina")
    elif choice_user == 'Piedra' and choice_maq == 'Tijeras':
        print("Gano Yo")
    elif choice_user == 'Papel' and choice_maq == 'Piedra':
        print ("Gano de nuevo yo")
    elif choice_user == 'Papel' and choice_maq == 'Tijeras':
        print("Gana la Maquina")
    elif choice_user == 'Tijeras' and choice_maq == 'Piedra':
        print("Gana la Maquina")
    elif choice_user == 'Tijeras' and choice_maq == 'Piedra':
        print("Gana maquina")
    else:
        print("Escribe bien no mms")

