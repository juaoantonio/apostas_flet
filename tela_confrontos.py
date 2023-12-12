import flet as ft
import controles as c
import tela_apostas


img_fla = ft.Image(
    src='apostas_flet/flamengo.png', 
    fit= ft.ImageFit.CONTAIN,
)
flamengo = ft.Container(
content= ft.Text(value='Flamengo')
)
placar_flamengo = ft.TextField(hint_text='0')
txt = ft.Text(value=f'{placar_flamengo.value}')

img_vasco = ft.Image(
    src='apostas_flet/vasco.png',
    fit= ft.ImageFit.CONTAIN,
)

def view():
    return ft.View(
        'tela_confrontos',
        [
            ft.Row(
                [
                    img_fla,
                    flamengo,
                    placar_flamengo,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    ft.TextField(hint_text='0'),
                    ft.Container(
                        content= ft.Text(value= 'Vasco')
                    ),
                    img_vasco,
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