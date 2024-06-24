"""
SCRIPT APENAS PARA TESTAR ALGUNS HOTKEYS
"""
import sys
import os
import keyboard as kb

def listen():
    test = sys.stdin.read()
    if test == 'right ctrl':
        os.close()



    # tecla = kb.read_key()

    # if tecla == "right ctrl":
    #     print("OK!")
    #     sys.exit()
    # else:
    #     print("apertou a letra errada")
    #     tecla == ''

listen()

# tecla = kb.read_hotkey()

# print(tecla)