import flet as ft
from views.navigationbar import add_item

class CustomCardTab:
    def __init__(self, image, text, price) -> None:
        self.image = image
        self.text = text
        self.price = price



    def view(self):
        content = ft.Card(
            ft.Container(
                bgcolor='white',
                width=400,
                content=ft.Row(
                    controls=[
                        ft.Container(
                            width=100,
                            content=ft.Image(
                                src=self.image
                            )
                        ),
                        ft.Container(
                            width=170,
                            content=ft.Text(
                                value=self.text,
                                width='bold',
                                color=ft.colors.BLACK
                            )
                        ),
                        ft.Container(
                            width=70,
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        self.price,
                                        color=ft.colors.BLACK
                                    ),
                                    ft.IconButton(icon=ft.icons.ADD, on_click=lambda _:add_item(self.image,self.text, self.price))
                                ]
                            )
                        )
                    ]
                )
            )
        )


        return content
    