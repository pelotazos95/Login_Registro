import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Registro"

    def abrir_dialog(message):
        dialog.content = ft.Text(message)
        dialog.open = True
        page.update()


    def cerrar_dialog(e):
        dialog.open = False
        page.update()

    def obtener_valores(e):
        email = email_tf.value
        if email == "":
            abrir_dialog("Tienes q selecionar un email")
            return

    contenedor = ft.Container(
        padding=10,
        bgcolor=ft.Colors.BLUE_500,
        width=page.width,
        height=page.height,
    )

    #def meter_datos(e):


    def volver(e):
        page.go("loginPage")

    nombre_tf = ft.TextField(label="Nombre")
    apellido_tf = ft.TextField(label="Apellidos")
    email_tf = ft.TextField(label="Email")
    contrasena_tf = ft.TextField(label="Contraseña")
    datos = ft.FilledButton("Finalizar Registro", on_click=obtener_valores)#, on_click = meter_datos())
    dialog = ft.AlertDialog(modal=True, title=ft.Text("Informacion"), content=ft.Text("Hola"),
                       actions=[ft.TextButton("Aceptar",on_click=cerrar_dialog),])
    volver_btn = ft.FilledButton(text="Volver al Login",on_click=volver)

    columna = ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("REGISTRO"),
            nombre_tf,
            apellido_tf,
            email_tf,
            contrasena_tf,
            datos,
            volver_btn,
        ]
    )
    fila = ft.Row(controls=[columna],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    contenedor.content = fila
    page.overlay.append(dialog)
    page.add(contenedor)

    return columna

ft.app(target=main, view=ft.WEB_BROWSER)