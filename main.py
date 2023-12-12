import flet as ft
import controles as c
# import views as vi

def main(page: ft.Page):
    c.init(page)
    page.title = "Apostas da Rodada"
    page.on_route_change = c.route_change
    page.theme_mode = "light"
    page.go("0")
    

ft.app(target=main)
