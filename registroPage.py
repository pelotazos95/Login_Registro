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

    def selecionar_fecha(e):
        fecha_tx.value = f"Fecha: {fecha_dp.value.day}/{fecha_dp.value.month}/{fecha_dp.value.year}"
        page.update()

    def abrir_selector(e):
        fecha_dp.open = True
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

    def volver(e):
        page.go("/main")

    nombre_tf = ft.TextField(label="Nombre")
    apellido_tf = ft.TextField(label="Apellidos")
    email_tf = ft.TextField(label="Email")
    contrasena_tf = ft.TextField(label="Contraseña")
    dialog = ft.AlertDialog(modal=True, title=ft.Text("Informacion"), content=ft.Text("Hola"),
                       actions=[ft.TextButton("Aceptar",on_click=cerrar_dialog),])
    volver_btn = ft.ElevatedButton(text="Volver a Navegacion",on_click=volver)

    columna = ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("REGISTRO"),
            nombre_tf,
            apellido_tf,
            email_tf,
            contrasena_tf,
            ft.ElevatedButton("Crear Tarea", on_click=obtener_valores),
            volver_btn,
        ]
    )
    fila = ft.Row(controls=[columna],
        alignment=ft.MainAxisAlignment.CENTER,
    )




    contenedor.content = fila
    page.overlay.append(dialog)
    page.add(contenedor)


ft.app(target=main, view=ft.WEB_BROWSER)