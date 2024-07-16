# Passo 1 - Entrar no sistema da empresa
    #link: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHFHX3M2U1U2dmg4QjBqaGhzN19MMnk1M2taZ3xBQ3Jtc0trYl9wcU0zSWxyTi03c1FmVE82V0c5RzZIN0Q0ajlKcTNsekNHLWlqQk41TFd2Z1Axd29LeF9jZnFzWnRDMTJLTEVGZU9uaUEta29JQ3V3d3hOcXZhaUhya1pXY1FUaVJVV1FEVm5JZHFFdkdtdUZXWQ&q=https%3A%2F%2Fdlp.hashtagtreinamentos.com%2Fpython%2Fintensivao%2Flogin&v=qbZsaBMxCJI
# Passo 2 - Fazer login
# Passo 3 - Pegar/Importar a base de dados
# Passo 4 - Cadastrar um produto
# Passo 5 - Repetir o passo 4 ate cadastrar todos os produtos

# pip install pyaoutogui
# /
# pandas openpyxl numpy

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - combinação de teclas (Ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5

# Passo 1 - Entrar no sistema da empresa
 # abrir o navegador
pyautogui.click(778, 1059)



# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2 - Fazer login
pyautogui.click(1232,448)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("luissilvassantos@gmail.com")

# passar para o campo da senha

pyautogui.press("tab")
pyautogui.write("Luisfilipe20")
pyautogui.click(1377,638)

time.sleep(3)

# Passo 3 - Pegar/Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4 - Cadastrar um produto
for linha in tabela.index: 
    #codigo

    pyautogui.click(1163,311)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    # marca

    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    # tipo

    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    # categoria

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    # preco_unitario

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    # custo

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])  
    pyautogui.write(custo)
    # obs

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    # enviar

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)
       