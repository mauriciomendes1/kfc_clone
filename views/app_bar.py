import flet as ft


def appBar(page, ft=ft):
    content = ft.AppBar(
        bgcolor='#E3002B',
        toolbar_height=70,
        title=ft.Row(
            controls=[
                ft.Container(
                    border=ft.border.all(2, 'white'),
                    width=90,
                    height=29,
                    border_radius=ft.border_radius.all(30),
                    alignment=ft.alignment.center,
                    content=ft.Text('Location', size=14)
                ),
                ft.Container(
                    width=90,
                    height=50,
                    content=ft.Image(
                        src='imagens/kfc.png'
                    )
                )
            ],
            alignment='spaceBetween'
        )
    )

    return content