import flet as ft
from controls.custom_card_pedido import CustomCardPedido

soma_total = 0
item = ft.Column(scroll='auto')

total = ft.Text('0,00'.format(soma_total), size=20, color='black')
msg = ft.Text('')
snack = ft.SnackBar(msg)

calc_total = []

nav = ft.NavigationBar(
    height=50,
    bgcolor='#E3002B',
    destinations=[
        ft.NavigationDestination(icon=ft.icons.MENU),
        ft.NavigationDestination(icon=ft.icons.SHOPPING_CART),
        ft.NavigationDestination(icon=ft.icons.SETTINGS)
    ],
    on_change= lambda e:show_market(e)
    
)



market = ft.BottomSheet(
    content=ft.Container(
        bgcolor='white',
        content=ft.Column(
            controls=[
                ft.Row(
                    height=50,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            'Itens do Pedido',
                            size=30,
                            width='bold',
                            color='black'
                            )
                    ]
                ),
                ft.Container(
                    height=250,
                    content=ft.Column(
                        scroll='auto',
                        controls=[
                            item
                        ]
                    )
                ),
                ft.Container(
                    margin=10,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        'Finalizar compra',
                                        color='white',
                                        bgcolor='#E3002B'),
                                    ft.Container(
                                        margin=20,
                                        content=ft.Row(
                                            controls=[
                                                ft.Text(
                                                    'Total R$', 
                                                    size=20, 
                                                    color='black'
                                                ),
                                                total
                                            ]
                                        )
                                    )
                                ],
                            )
                        ]
                    )
                )
            ]
        )
    )
)


def show_market(e):

    match e.control.selected_index:
        case 0:
            print('Menu')
        case 1:
            market.open = True
            calcular_total()
            market.update()
        case 2:
            print('Settings')

def add_item(image, text, price):
    global calc_total

    msg.value = text + ' ADICIONADO!'
    msg.update()

    snack.open = True
    snack.update()

    preco = price.split('R$')
    preco_format = preco[1].replace(',', '.')
    calc_total.append(float(preco_format))
    item.controls.append(CustomCardPedido(image, text, price).view())



def delete_item():
    for i in item.controls:
        print(i)

def calcular_total():
    global soma_total, total

    soma_total = sum(calc_total)
    
    total.value = '{:.2f}'.format(soma_total)
    total.update()
