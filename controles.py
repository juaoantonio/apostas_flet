import flet as ft
import tela_confrontos
import tela_apostas

def init(p):
    global page, telas
    page = p
    telas = {
        '0': tela_confrontos.view(),
        '1': tela_apostas.view()
    }

def route_change(route):
    page.views.clear()    
    page.views.append(
        telas[page.route]
    )        
    page.update()