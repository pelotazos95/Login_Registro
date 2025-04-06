import flet as ft
import ddbb
import infoPage
import loginPage
import principal
import registroPage

def main(page: ft.Page):
    page.title = "APP REGISTROS/LOGIN"

    def route_change(e):
        page.views.clear()

        if page.route == "/login":
            page.views.append(
                ft.View(
                    route="/login",
                    controls=[loginPage.main(page)]
                )
            )
        elif page.route == "/registro":
            page.views.append(
                ft.View(
                    route="/registro",
                    controls=[registroPage.main(page)]
                )
            )
        elif page.route == "/infoPage":
            page.views.append(
                ft.View(
                    route="/infoPage",
                    controls=[infoPage.main(page)]
                )
            )

        page.update()


    page.on_route_change = route_change
    page.go("/login")

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=30018)