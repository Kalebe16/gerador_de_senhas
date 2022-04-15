import PySimpleGUI as sg
import random
import os
import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')


tema = "DarkAmber"
count = 0


def criar_janela():
    sg.theme(tema)
    

    layout = [
        [sg.Text("Site/Software:", size=(10, 1)), sg.Input("", key="-SITE-", size=(20, 1))],
        [sg.Text("Usuario/Email:", size=(10, 1)), sg.Input("", key="-USUARIO-", size=(20, 1))],
        [sg.Text("Quantidade de caracteres:"), sg.Combo(values=list(range(30)), key="-TOTALCARACTERES-", default_value="1", size=(3, 1))],           
        [sg.Output(size=(32, 5))],
        [sg.Button("Gerar Senha"), sg.Button("Salvar Senha"), sg.Button(image_filename=r"imgautofalante.png", image_size=(24, 24), key="-MUSICA-")]
    ]
    
    return sg.Window("Senhas Fortes", layout=layout, finalize=True, element_justification="center")


def criar_senha(values):
    lista_caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
    caracteres = random.choices(lista_caracteres, k=int(values["-TOTALCARACTERES-"])) 
    nova_senha = ''.join(caracteres) 
    return nova_senha
    
    
def salvar_senha(senha, values):
    with open("senhas.txt", "a", newline="") as arquivo:
        arquivo.write(f"\nSite: {values['-SITE-']} \nUsuario: {values['-USUARIO-']} \nSenha: {senha}\n")
    print("Arquivo salvo")

def player_musica():
    if count == 1:
        pygame.mixer.music.play(loops=-1) # toca a musica e a repete infinitamente
    elif count % 2 == 0:
        pygame.mixer.music.pause() # pausa a musica temporariamente
    elif count % 2 != 0:
        pygame.mixer.music.unpause() # retoma a musica de onde tinha parado
    
        
janela = criar_janela()

while True:
    window, event, values = sg.read_all_windows(timeout=1)

    if window != janela:
        continue

    if event == sg.WIN_CLOSED:
        break
    if event == "Gerar Senha":
        senha = criar_senha(values)
        print(senha)
    if event == "Salvar Senha":
        salvar_senha(senha, values)
    if event == "-MUSICA-":
        count += 1
        player_musica()
