import pyautogui
import webbrowser
from time import sleep

def Logout():
    pyautogui.click(2010,742, duration=2)
    pyautogui.click(1960,989, duration=2)
    pyautogui.click(1972,927, duration=2)


while True:

    webbrowser.open_new_tab('https://www.instagram.com/')
    sleep(10)

    #digitar ususrario
    pyautogui.click(3057,361, duration=1) 
    pyautogui.typewrite('pobreporcarros')
    sleep(1)

    #digitar senha 
    pyautogui.click(3041,404, duration=1) 
    pyautogui.typewrite('Jesus147096')
    sleep(1)

    #clicar em entrar
    pyautogui.click(3078,454, duration=2)
    sleep(10)

    #eliminar a janela de salvar informações
    pyautogui.click(3037,604, duration=2)
    sleep(10)

    # ir em ate pesquisar
    pyautogui.click(2007,257, duration=4)
    pyautogui.click(2065,184, duration=2)
    pyautogui.typewrite('nike')
    sleep(10)

    #clicar no instagran da nike
    pyautogui.click(2088,260, duration=2)
    sleep(10)

    #ir ate a ultima foto
    pyautogui.click(2735,676, duration=2)
    sleep(10)

    #verificar se ja curti
    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    sleep(1)

    #se tiver curtido fazer nada e apusar o boot por 24 horas 
    if coracao is not None:
        Logout()
        sleep(86400)

    #se nao tiver curtido , curtir a foto
    elif coracao == None:
        pyautogui.click(3019,889, duration=2)
        sleep(5)

        pyautogui.click(3060,890, duration=2)
        sleep(2)
        pyautogui.click(33113,990, duration=2)
        sleep(2)
        pyautogui.typewrite('Gostei De mais')
        sleep(3)
        pyautogui.click(3449,987, duration=2)
        sleep(10)
        Logout()
        sleep(86400)