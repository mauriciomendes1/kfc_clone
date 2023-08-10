import flet as ft
from views.navigationbar import add_item

class CustomCard:
    def __init__(self, text, price_value, src):
        super().__init__()
        self.text = text
        self.price_value = price_value
        self.src = src
        self.image = ft.Image(self.src, border_radius=ft.border_radius.only(top_left=20, top_right=20))
        self.title = ft.Text(self.text, width='bold')
        self.price = ft.Text(self.price_value, width='bold')

    def view(self):
        content = ft.Card(
                color='#E3002B',
                content=ft.Container(
                    border=ft.border.all(1),
                    border_radius=ft.border_radius.all(20),
                    width=150,
                    height=200,
                    bgcolor='#E3002B',
                    content=ft.Column(
                        controls=[
                            self.image,
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=ft.padding.all(5),
                                        height=50,
                                        alignment=ft.alignment.center,
                                        content=self.title
                                    )
                                ]
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        padding=ft.padding.all(5),
                                        content=self.price
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.ADD,
                                        on_click=lambda _:add_item(self.src, self.text, self.price_value)
                                    )
                                ]
                            )
                        ]
                    )
                )
            )
        return content