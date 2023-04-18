import pyautogui

screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')

# Explicação do código:
# import pyautogui : importa a biblioteca PyAutoGUI, que é uma biblioteca Python que fornece funções 
                        # para automatizar a interação com a interface gráfica do usuário (GUI) 
                        # em sistemas operacionais Windows, macOS e Linux.

# screenshot = pyautogui.screenshot(): Essa linha de código chama a função screenshot() da biblioteca
                                        #  PyAutoGUI para tirar uma captura de tela do monitor. 
                                        # A imagem capturada é armazenada em uma variável chamada 
                                        # screenshot.

# screenshot.save('screenshot.png'): Essa linha de código chama o método save() do objeto screenshot 
                                        # para salvar a captura de tela como uma imagem PNG. 
                                        # O nome do arquivo é definido como "screenshot.png", que é 
                                        # o nome do arquivo de saída. 

# Você pode alterar o nome do arquivo e o formato da imagem (por exemplo, JPEG) conforme necessário.

# Após a execução desse código, uma captura de tela do monitor será tirada e salva como 
    # uma imagem PNG com o nome "screenshot.png" no diretório onde o código está sendo executado.