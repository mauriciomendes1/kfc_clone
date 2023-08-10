import flet as ft
from data.data import baldes, promocoes, lancamentos
from controls.custom_card_tab import CustomCardTab

    
balde = ft.Column(scroll='auto')
promo = ft.Column(scroll='auto')
lancamento = ft.Column(scroll='auto')


for x in baldes:
    balde.controls.append(
       CustomCardTab(x['image'], x['title'].upper(), x['price']).view()
    )

for i in promocoes:
    promo.controls.append(
        CustomCardTab(i['image'], i['title'].upper(), i['price']).view()
    )

for i in lancamentos:
    lancamento.controls.append(
        CustomCardTab(i['image'], i['title'].upper(), i['price']).view()
    )


tabs_menu = ft.Tabs(
    selected_index=0,
    expand=1,
    tabs=[
        ft.Tab(
            text='Lançamentos',
            content=ft.Container(
                bgcolor='white',
                content=ft.Column(
                    scroll='auto',
                    controls=[
                        lancamento
                    ]
                )
            )
            ),
        ft.Tab(
            text='Promoções',
            content=ft.Container(
                bgcolor='white',
                content=ft.Column(
                    scroll='auto',
                    controls=[
                        promo
                    ]
                )
            )
        ),
        ft.Tab(
            text='Baldes',
            content=ft.Container(
                bgcolor='white',
                content=ft.Column(
                    scroll='auto',
                    controls=[
                        balde
                    ]
                )
            )
        ),
        ft.Tab(
            text='Combos Sanduíches',
            content=ft.Container(
                bgcolor='white',
                content=ft.Column(
                    scroll='auto',
                    controls=[
                        
                    ]
                )
            )
        )
    ]
)

