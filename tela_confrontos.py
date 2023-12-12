import flet as ft
import controles as c
import tela_apostas

#Criação da parte do atletico paranaense
img_atl_pr = ft.Image(
    src='apostas_flet/icones/atletico_pr.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
atl_pr = ft.Container(
content= ft.Text(value='Atlético-Pr')
)

#criação dos textfields para dados das apostas
global placar_atl_pr, placar_atl_go
placar_atl_pr = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_atl_go = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

#criação da parte do atletico go
img_atl_go = ft.Image(
    src='apostas_flet/icones/Atlético_Goianiense.svg.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
atl_go = ft.Container(
content= ft.Text(value='Atlético-Go')
)

#Criação da parte do atletico mineiro
img_atl_mg = ft.Image(
    src='apostas_flet/icones/atl_mg.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
atl_mg = ft.Container(
content= ft.Text(value='Atletico-Mg')
)

#criação dos textfields para dados das apostas
global placar_atl_mg, placar_bahia
placar_atl_mg = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_bahia = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

#criação da parte do bahia
img_bahia = ft.Image(
    src='apostas_flet/icones/bahia.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
bahia = ft.Container(
content= ft.Text(value='Bahia')
)

#Criação da parte do botafogo
img_bot = ft.Image(
    src='apostas_flet/icones/Botafogo.svg.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
bot = ft.Container(
content= ft.Text(value='Botafogo')
)

#criação dos textfields para dados das apostas
global placar_bot, placar_braga
placar_bot = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_braga = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

#criação da parte do bahia
img_braga = ft.Image(
    src='apostas_flet/icones/bragantino.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
braga = ft.Container(
content= ft.Text(value='Bragantino')
)

#Criação da parte do corinthians
img_cor = ft.Image(
    src='apostas_flet/icones/corinthians.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
cor = ft.Container(
content= ft.Text(value='Corinthians')
)

#criação dos textfields para dados das apostas
global placar_cor, placar_cric
placar_cor = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_cric = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

#criação da parte do criciuma
img_cric = ft.Image(
    src='apostas_flet/icones/criciuma.svg.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
cric = ft.Container(
content= ft.Text(value='Criciuma')
)

#Criação da parte do cruzeiro
img_cru = ft.Image(
    src='apostas_flet/icones/cruzeiro.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
cru = ft.Container(
content= ft.Text(value='Cruzeiro')
)

#criação dos textfields para dados das apostas
global placar_cru, placar_cuiaba
placar_cru = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_cuiaba = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

#criação da parte do cuiaba
img_cuiaba = ft.Image(
    src='apostas_flet/icones/cuiaba.svg.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
cuiaba = ft.Container(
content= ft.Text(value='Cuiaba')
)

#Criação da parte do flamengo
img_fla = ft.Image(
    src='apostas_flet/icones/flamengo.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
fla = ft.Container(
content= ft.Text(value='Flamengo')
)

#criação dos textfields para dados das apostas
global placar_fla, placar_flu
placar_fla = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_flu = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

#criação da parte do cuiaba
img_flu = ft.Image(
    src='apostas_flet/icones/fluminense.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
flu = ft.Container(
content= ft.Text(value='Fluminense')
)

#Criação da parte do fortaleza
img_fort = ft.Image(
    src='apostas_flet/icones/fortaleza.svg.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
fort = ft.Container(
content= ft.Text(value='Fortaleza')
)

#criação dos textfields para dados das apostas
global placar_fort, placar_gre
placar_fort = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_gre = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

#criação da parte do cuiaba
img_gre = ft.Image(
    src='apostas_flet/icones/Gremio.svg.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
gre = ft.Container(
content= ft.Text(value='Gremio')
)

#Criação da parte do Internacional
img_inter = ft.Image(
    src='apostas_flet/icones/inter.svg.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
inter = ft.Container(
content= ft.Text(value='Internacional')
)

#criação dos textfields para dados das apostas
global placar_inter, placar_Juv
placar_inter = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_juv = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

#criação da parte do cuiaba
img_juv = ft.Image(
    src='apostas_flet/icones/juventude.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
juv = ft.Container(
content= ft.Text(value='Juventude')
)

#Criação da parte do palmeiras
img_pal = ft.Image(
    src='apostas_flet/icones/palmeiras.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
pal = ft.Container(
content= ft.Text(value='Palmeiras')
)

#criação dos textfields para dados das apostas
global placar_pal, placar_sp
placar_pal = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_sp = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

#criação da parte do cuiaba
img_sp = ft.Image(
    src='apostas_flet/icones/sao_paulo.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
sp = ft.Container(
content= ft.Text(value='Juventude')
)

#Criação da parte do vasco
img_vas = ft.Image(
    src='apostas_flet/icones/vasco.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
vasco = ft.Container(
content= ft.Text(value='Vasco')
)

#criação dos textfields para dados das apostas
global placar_vas, placar_vit
placar_vas = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)
placar_vit = ft.TextField(hint_text='N', width= 50, text_align= ft.alignment.center)

#criação da parte do vitoria
img_vit = ft.Image(
    src='apostas_flet/icones/vitoria.png',
    height= 70,
    width= 70, 
    fit= ft.ImageFit.CONTAIN,
)
vit = ft.Container(
content= ft.Text(value='Juventude')
)

def view():
    return ft.View(
        'tela_confrontos',
        [
            ft.Column(
                [
                    ft.Row(
                [
                    img_atl_pr,
                    atl_pr,
                    placar_atl_pr,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    placar_atl_go,
                    atl_go,
                    img_atl_go,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_atl_pr.value, placar_atl_go.value)
                    ), #printa na tela e salva os valores colocados no textfield
                ]
            ),
            ft.Row(
                [
                    img_atl_mg,
                    atl_mg,
                    placar_atl_mg,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    placar_bahia,
                    bahia,
                    img_bahia,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_atl_mg.value, placar_bahia.value)
                    ), #printa na tela e salva os valores colocados no textfield
                ]
            ),
            ft.Row(
                [
                    img_bot,
                    bot,
                    placar_bot,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    placar_braga,
                    braga,
                    img_braga,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_bot.value, placar_braga.value)
                    ), #printa na tela e salva os valores colocados no textfield
                ]
            ),
            ft.Row(
                [
                    img_cor,
                    cor,
                    placar_cor,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    placar_cric,
                    cric,
                    img_cric,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_cor.value, placar_cric.value)
                    ), #printa na tela e salva os valores colocados no textfield
                ]
            ),
            ft.Row(
                [
                    img_cru,
                    cru,
                    placar_cru,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    placar_cuiaba,
                    cuiaba,
                    img_cuiaba,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_cru.value, placar_cuiaba.value)
                    ), #printa na tela e salva os valores colocados no textfield
                ]
            ),
            ft.Row(
                [
                    img_fla,
                    fla,
                    placar_fla,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    placar_flu,
                    flu,
                    img_flu,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_fla.value, placar_flu.value)
                    ), #printa na tela e salva os valores colocados no textfield
                ]
            ),
            ft.Row(
                [
                    img_fort,
                    fort,
                    placar_fort,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    placar_gre,
                    gre,
                    img_gre,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_fort.value, placar_gre.value)
                    ), #printa na tela e salva os valores colocados no textfield
                ]
            ),
            ft.Row(
                [
                    img_inter,
                    inter,
                    placar_inter,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    placar_juv,
                    juv,
                    img_juv,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_inter.value, placar_juv.value)
                    ), #printa na tela e salva os valores colocados no textfield
                ]
            ),
            ft.Row(
                [
                    img_pal,
                    pal,
                    placar_pal,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    placar_sp,
                    sp,
                    img_sp,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_pal.value, placar_sp.value)
                    ), #printa na tela e salva os valores colocados no textfield
                ]
            ),
            ft.Row(
                [
                    img_vas,
                    vasco,
                    placar_vas,
                    ft.Container(
                        content = ft.Text(value = 'x')
                    ),
                    placar_vit,
                    vit,
                    img_vit,
                    ft.ElevatedButton(
                        text='Salvar', on_click= lambda _: print(placar_vas.value, placar_vit.value)
                    ), #printa na tela e salva os valores colocados no textfield
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
            ),
                ],
                scroll= 'always', expand= True
            )
        ]
    )