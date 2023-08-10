import flet as ft
from data.data import menu_data
from controls.custom_card import CustomCard

def page_title(page, ft=ft):

    def get_valor(valor):
        print(valor)
 
    produto = ft.Row()

    for x in menu_data:
       
        produto.controls.append(
            CustomCard(x['title'].upper(), x['price'], x['image']).view()
        )

    content = ft.Container(
        padding=ft.padding.only(top=20),
        width=1920,
        bgcolor='#E3002B',
        content=ft.Column(
            controls=[
                ft.Container(
                    margin=ft.margin.only(left=10),
                    content=ft.Text('No Restaurante', color='white', size=30, weight='bold'),
                ),
                ft.Row(
                    controls=[
                        produto
                    ], scroll='auto'
                )
            ]
        )
    )

    return content