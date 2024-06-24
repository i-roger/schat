import threading
import socket
import keyboard as kb
import os
import sys

def escape():
    os.system('cls')

kb.on_press_key("right ctrl", lambda _: escape()) #Function Lambda

os.system('color 08')
alias = input('Who are you? >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('172.16.73.243', 59000))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "alias?":
                client.send(alias.encode('utf-8'))

            else:
                print(message)

        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:

        message = f'{alias}: {input("")}'

        if message == f'{alias}: exit': ### Clean and close
            os.system('cls')
            client.close()
            sys.exit()
        
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()