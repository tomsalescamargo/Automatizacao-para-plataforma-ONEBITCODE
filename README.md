**Automatizacao-para-plataforma-ONEBITCODE**

Este repositório apresenta uma solução para um desafio do curso ONEBITCODE. Durante a troca de plataformas, a marcação do progresso individual das aulas vistas pelos alunos foi perdida. O objetivo é criar uma ferramenta que automatize a atualização desse progresso, permitindo que cada aluno marque como vistas suas aulas perdidas na nova plataforma.

**Modo de uso**

Para usar este script, você precisa instalar o pyautogui. 
Para isso, abra o terminal no diretório atual e execute o seguinte comando:
`pip install pyautogui`


Após isso, inicialize o programa e siga os seguintes passos:

  **1. Selecione a Aula:** Entre na plataforma da ONEBITCODE e selecione a aula em que deseja iniciar a marcação.

  **2. Identifique a Posição do Botão:** Antes de iniciar a automação, é necessário descobrir a posição do botão na tela do seu computador. Ao iniciar o programa, pressione a tecla "ENTER" e, em seguida, posicione o mouse sobre o botão "Concluir aula", na página da aula que você acabou de selecionar. Você terá 5 segundos para garantir que o pyautogui capture a posição corretamente.

  **3. Defina a Quantidade:** Informe quantas aulas você deseja marcar como vistas.

  **4. Volte à plataforma:** Após informar a quantidade, inicia-se a automação, e você terá 5 segundos para reabrir o navegador na página correta.


Caso deseje interromper a automação, deixe seu mouse parado no canto superior esquerdo da tela




