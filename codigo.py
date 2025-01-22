# pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

# Passo 1: Abrir o sitema da empresa

# Aperta a tecla windows
pyautogui.press("win")

# Digitar o texto chrome
pyautogui.write("chrome")

# Apertar enter
pyautogui.press("enter")

# Entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Pedir para o computador esperar 2 segundos
time.sleep(2)

# Passo 2: Fazer o login
pyautogui.click(x=1796, y=374)
pyautogui.write("pythonpowerup@gmail.com")

pyautogui.press("tab") # Passar para o campo da senha
pyautogui.write("minhasenha123")

pyautogui.press("tab") # Passar para o botão "Logar"
pyautogui.press("enter")

# Passo 3: Importar a base de dados
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")

# Pedir para o computador esperar 2 segundos
time.sleep(2)

# Passo 4: Cadastrar 1 produto

for linha in tabela.index:
    pyautogui.click(x=1799, y=259) # Clicar do 1 campo

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo 
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) 
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter") # Apertar para enviar

    pyautogui.scroll(10000)

# Passo 5: Repetir o passo 4 até acaba os produtos