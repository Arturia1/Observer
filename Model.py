
import flet as ft # importar
from Observer import *


def main(pagina): # criar a função principal/main
    
    texto = ft.Text("Storage Manager")



    titulo_popup3 = ft.Text("Altere o quantitativo de Camisas.")  
    camisa_quantitativo = ft.TextField(label="Quantas unidades?")
    botao_entrar3 = ft.ElevatedButton("Confirmar")

    popup3 = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup3,
        content=camisa_quantitativo,
        actions=[botao_entrar3]
    )
    
    def abrir_popup3(evento):
        pagina.dialog = popup3
        popup3.open = True
        pagina.update()

    titulo_popup2 = ft.Text("Senha")  
    senha_usuario = ft.TextField(label="sua senha", password=True, can_reveal_password=True, on_submit= abrir_popup3)
    botao_entrar2 = ft.ElevatedButton("Confirmar", on_click= abrir_popup3)
    
    
    popup2 = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup2,
        content=senha_usuario,
        actions=[botao_entrar2]
    )
    
    def abrir_popup2(evento):
        pagina.dialog = popup2
        popup2.open = True
        pagina.update()
    
    titulo_popup = ft.Text("Usuário")
    nome_usuario = ft.TextField(label="Seu nome", on_submit = abrir_popup2)   
    botao_entrar = ft.ElevatedButton("Confirmar", on_click = abrir_popup2)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar consulta", on_click = abrir_popup)
    
    
    pagina.add(texto)
    pagina.add(botao_iniciar)

def new_func():
    return "Sua senha"

    

ft.app(target=main) # criar o app chamando a função principa