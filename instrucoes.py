import flet as ft
import controles as c
import tela_confrontos
import instrucoes
import tela_apostas

def view():
    return ft.View(
        'intrucoes',
        [
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(value='Sigas as Seguintes instruções para realizar a aposta')
                    ]
                    
                ),
                ft.Column(
                    [
                        ft.Container(content= ft.Text(value='1- Coloque no placar o seu palpite, e em seguida, aperte no botão SALVAR, para salvar seus palpites.')),
                        ft.Container(content=ft.Text(value='2- Coloque o valor em reais e aperte em SALVAR')),
                        ft.Container(content=ft.Text(value='3- Aperte o botão IR PARA APOSTAS, para ver seus resultados')),
                        ft.Container(content=ft.Text(value='')),
                        ft.Container(content=ft.Text(value='É Importante lembrar que apostas são proibidas para menores de 18, você pode perder seu dinheiro e NÂO DAMOS REEMBOLSO')),
                    ]
                ),
                ft.ElevatedButton(text='Voltar para apostas', on_click= lambda _: c.page.go('0'))
            ]
        )
        ]
    )