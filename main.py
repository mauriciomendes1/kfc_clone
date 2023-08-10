import flet as ft
from views.app_bar import appBar
from views.page_title import page_title
from views.tabbar import tabs_menu
from views.navigationbar import nav, market, snack

def main(page:ft.Page):
    page.window_width = 400
    page.appbar = appBar(page)
    page.navigation_bar = nav
    page.snack_bar = snack

    page.add(
        #CARROSSEL SUPERIOR
        page_title(page),
        # TABS BAR
        tabs_menu,
        #CARRO DE COMPRAS
        market
    )

    

ft.app(target=main)