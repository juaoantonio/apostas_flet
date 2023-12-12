import flet as ft
import controles as c
import tela_apostas

flamengo = ft.Container(
content= ft.Text(value='Flamengo')
)
placar_flamengo = ft.TextField(hint_text='0')
txt = ft.Text(value=f'{placar_flamengo.value}')

def view():
    return ft.View(
        'tela_confrontos',
        [
            ft.Row(
                [
                    flamengo,
                    placar_flamengo,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    ft.TextField(hint_text='0'),
                    ft.Container(
                        content= ft.Text(value= 'Vasco')
                    )
                ]
            ),
            ft.Row(
                [
                    ft.Container(
                        content= ft.Text(value= 'Adicione valor da aposta: ')
                    ),
                    ft.TextField(hint_text='valor'),
                ]
            ),
            ft.Row(
                [
                    ft.Container(
                        content= ft.ElevatedButton(text= 'ir para apostas', on_click= lambda _: c.page.go('1')),
                    )
                ]
            )
            
        ]
    )