import flet as ft
import controles as c
import tela_confrontos as tc

valor_jogo_1 = '3 x 2'

def view():
    return ft.View(
        'tela_apostas',
        [
            ft.Row(
                [
                    ft.Container(
                        content= ft.Text(value= f'Atletico-pr vs Atletico-go: {valor_jogo_1}')
                    ),
                    ft.Container(
                        content= ft.Text(value=f'Sua aposta: ')
                    )
                ]
            ),
            ft.Row(
                [
                    ft.Container(
                        content= ft.ElevatedButton(text='Voltar aos confrontos', on_click= lambda _: c.page.go('0')),
                    )
                ]
            )
        ]
    )