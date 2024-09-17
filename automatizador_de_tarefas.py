import pyautogui
import time

#Passo 1 - Entrar no sistema
#Abrir navegador
pyautogui.PAUSE = 0.5
pyautogui.press ("win")  
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)

#passo 2 - fazer login
pyautogui.click(x=832,y=464)
pyautogui.hotkey("ctrl","a")
pyautogui.write("exemplo.gmail.com")

# fazer senha
pyautogui.press("tab")
pyautogui.write("senha")

pyautogui.click(x=941,y=669)

time.sleep(3)

#passo 3 - importar base de dados
import pandas 
tabela = pandas.read_csv("produtos.csv")

    # passo 4 - cadastar o produto e repetir em loop
for intens in tabela.index:
    # codigo
    pyautogui.click(x=656,y=337)
    codigo = str(tabela.loc[intens,"codigo"])
    pyautogui.write(codigo)

    # marca
    marca = str(tabela.loc[intens,"marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    # tipo
    tipo = str(tabela.loc[intens,"tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    # categoria
    categoria = str(tabela.loc[intens,"categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    # preco_unitario
    preco = str(tabela.loc[intens,"preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    # custo
    custo = str(tabela.loc[intens,"custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[intens,"obs"])
    if  obs != "nan":
        pyautogui.write(obs)

    #enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(2000)


