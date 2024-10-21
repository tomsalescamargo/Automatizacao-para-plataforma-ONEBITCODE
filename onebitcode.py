import pyautogui
import time


pyautogui.PAUSE = 0.3

# Instruções para o usuário
print("***OLÁ, ESSE É O SCRIPT DE RECUPERAÇÃO DA MARCAÇÃO DE PROGRESSO NA COMUNIDADE ONEBITCODE***")
print("Feito por: Tom Sales")
print()
print("ATENÇÃO! POR FAVOR SEJA HONESTO, UTILIZE SOMENTE NAS AULAS QUE FORAM REALMENTE PERDIDAS NA TROCA DE PLATAFORMA.")
print()
print('ETAPAS/MODO DE USO DO PROGRAMA:')
print()
print('  1. Selecione a Aula: Entre na plataforma da ONEBITCODE e selecione a aula em que deseja iniciar a marcação.')
print()

print('  2. Identifique a Posição do Botão: Antes de iniciar a automação, é necessário descobrir a posição do botão na tela do seu computador. Pressione a tecla "ENTER" e, em seguida, posicione o mouse sobre o botão "Concluir aula", na página da aula que você acabou de selecionar. Você terá 5 segundos para garantir que o pyautogui capture a posição corretamente.')
print()
# Verificação para pressionar Enter
while True:
    enter_input = input('Pressione a tecla "enter" quando estiver pronto para posicionar o mouse no botão: ')
    print()

    if enter_input == '':
        break  # Sai do loop se o usuário pressionar Enter
    else:
        print('Valor inserido inválido, pressione a tecla enter quando estiver pronto.')
        print()

time.sleep(5)  # Tempo para o usuário posicionar o mouse

# Captura a posição atual do mouse
button_position = pyautogui.position()
print(f"Posição do botão capturada: {button_position}")
print()


print()
print('  3. Defina a Quantidade: Será preciso informar quantas aulas você deseja marcar como vistas. ATENÇÃO! Ao informar a quantidade, inicia-se a automação, e você terá 5 segundos para reabrir o navegador na página correta.')
print()
print('**Caso deseje interromper a automação, deixe seu mouse parado no canto superior esquerdo da tela')
print()
print()


# Captura a posição atual do mouse
button_position = pyautogui.position()
print(f"Posição do botão capturada: {button_position}")
print()

# Armazena a quantidade de aulas que o usuário deseja marcar
while True:
    classes_input = input('Quantas aulas você quer marcar? ')
    print()

    try:
        classes = int(classes_input)

        if classes < 1:
            print('Por favor, insira um número inteiro, maior que 0.')
            print()
            raise ValueError
        else:
            print("INICIANDO A AUTOMAÇÃO, VÁ PARA A PÁGINA DA AULA!")
            # Realiza os cliques
            for i in range(classes):
                time.sleep(5)  # Delay antes de cada clique
                pyautogui.click(button_position)  # Clica na posição capturada

            print(f"{classes} aulas marcadas com sucesso")
            break  # Sai do loop

    except ValueError:
        print('Valor inserido inválido. Por favor, insira um número inteiro, maior que 0.')
        print()


