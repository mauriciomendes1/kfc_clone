import flet as ft
# from views.navigationbar import delete_item

class CustomCardPedido:
    def __init__(self, image, text, price) -> None:
        self.image = ft.Image(src=image, width=100, fit=ft.ImageFit.CONTAIN)
        self.text = ft.Text(value=text, size=14, color='black', width=150)
        self.price = ft.Text(price, size=15, width=65, color='black')


    def view(self):
        content = ft.Card(
            content=ft.Container(
                bgcolor='white',
                border=ft.border.all(1, 'red'),
                content=ft.Row(
                    controls=[
                        self.image,
                        self.text,
                        self.price,
                        ft.Column(
                            alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.IconButton(icon=ft.icons.DELETE)
                            ]
                        )
                        
                    ],
                    # alignment='spaceBetween'
                )
            )
        )

        return content
    
    def delete(self):
        pass