import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Login"

    contenedor = ft.Container(
        padding=10,
        bgcolor=ft.Colors.BLUE_500,
        width=page.width,
        height=page.height,
    )

    def volver(e):
        page.go("registroPage")
        page.update()


    usuario_tf = ft.TextField(label="Usuario o Contraseña")
    contrasena_tf = ft.TextField(label="Contraseña")
    volver_btn = ft.FilledButton(text="Registrarse", on_click=volver)

    columna = ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("LOGIN"),
            usuario_tf,
            contrasena_tf,
            ft.FilledButton("Aceptar"),
            volver_btn,
        ]
    )
    fila = ft.Row(controls=[columna],
            alignment=ft.MainAxisAlignment.CENTER,
    )

    page.update()
    contenedor.content = fila
    page.add(contenedor)

    return columna

ft.app(target=main, view=ft.WEB_BROWSER)