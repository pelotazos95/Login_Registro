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
        page.go("/principal")
        page.update()

    def mostrar_mensaje(mensaje):
        print(mensaje)
        dialog.content = ft.Text(mensaje)
        dialog.open = True
        page.update()

    def selecionar_fecha(e):
        fecha_tx.value = f"Fecha: {fecha_dp.value.day}/{fecha_dp.value.month}/{fecha_dp.value.year}"
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


    usuario_tf = ft.TextField(label="Email",width=300)
    passwd_tf = ft.TextField(label="Contraseña",width=300)
    volver_btn = ft.FilledButton(text="Registrarse", on_click=volver)
    fecha_dp = ft.DatePicker(value=datetime.datetime.now(), on_change=selecionar_fecha)
    fecha_tx = ft.Text(f"Ultimo Login: {fecha_dp.value.day}/{fecha_dp.value.month}/{fecha_dp.value.year}")
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
            fecha_tx,
            ft.FilledButton("Aceptar", on_click = comprobar_datos),
            volver_btn,
        ]
    )
    fila = ft.Row(controls=[columna],
            alignment=ft.MainAxisAlignment.CENTER,
    )

    contenedor.content = fila
    page.overlay.append(dialog)
    page.add(contenedor)
    page.update()


    return columna