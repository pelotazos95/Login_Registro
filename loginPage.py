import flet as ft
import ddbb
import datetime

def main(page: ft.Page):
    page.title = "Login"

    contenedor = ft.Container(
        padding=10,
        bgcolor=ft.Colors.BLUE_500,
        width=page.width,
        height=page.height,
    )

    def cerrar_dialog(e):
        dialog.open = False
        page.update()

    def mostrar_mensaje(mensaje):
        print(mensaje)
        dialog.content = ft.Text(mensaje)
        dialog.open = True
        page.update()

    def comprobar_datos(e):
        email = usuario_tf.value
        password = passwd_tf.value
        mensaje = None
        if email == "" or email is None:
            mensaje = ("Tienes q selecionar un email")
        elif password == "" or password is None:
            mensaje = ("Tienes q indicar una contraseña")

        if mensaje is not None:
            mostrar_mensaje(mensaje)
            return

        ddbb.comprobar_usuario(email, password)
        mostrar_mensaje("USUARIO CORRECTO")

    def volver(e):
        page.go("/registro")
        page.update()


    usuario_tf = ft.TextField(label="Email")
    passwd_tf = ft.TextField(label="Contraseña")
    volver_btn = ft.FilledButton(text="Registrarse", on_click=volver)
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("YEAAAAAH BUDYYYYYYYY"),
        actions=[
            ft.TextButton("Aceptar", on_click=cerrar_dialog),
        ]
    )

    columna = ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("LOGIN"),
            usuario_tf,
            passwd_tf,
            ft.FilledButton("Aceptar", on_click = comprobar_datos),
            volver_btn,
        ]
    )
    fila = ft.Row(controls=[columna],
            alignment=ft.MainAxisAlignment.CENTER,
    )

    page.update()
    contenedor.content = fila
    page.overlay.append(dialog)
    page.add(contenedor)

    return columna