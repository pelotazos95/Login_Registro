import flet as ft
from flet.core import page

import loginPage
import registroPage

def main(page: ft.Page):
    page.title = "APP REGISTROS/LOGIN"

    def route_change(e):
        page.views.clear()

        if page.route == "/loginPage":
            page.views.append(
                ft.View(
                    route="/loginPage",
                    controls=[loginPage.main(page)]
                )
            )
        elif page.route == "/registroPage":
            page.views.append(
                ft.View(
                    route="/registroPage",
                    controls=[registroPage.main(page)]
                )
            )
        else:
            page.go("/loginPage")

        page.update()

    page.on_route_change = route_change
    page.go("/loginPage")

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, PORT = 8080)