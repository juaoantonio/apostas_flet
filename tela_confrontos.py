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

global placar_flamengo, placar_vasco
placar_flamengo = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_vasco = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

img_vasco = ft.Image(
    src='apostas_flet/vasco.png',
    fit= ft.ImageFit.CONTAIN,
)
vasco = ft.Container(
content= ft.Text(value='Vasco')
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
                    placar_vasco,
                    vasco,
                    img_vasco,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_flamengo.value, placar_vasco.value)
                    ),
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