import flet as ft
import controles as c
import tela_confrontos

def view():
    return ft.View(
        'tela_apostas',
        [
            ft.Row(
                [
                    ft.Container(
                        content= ft.ElevatedButton(text='Voltar aos confrontos', on_click= lambda _: c.page.go('0')),
                    )
                ]
            )
        ]
    )