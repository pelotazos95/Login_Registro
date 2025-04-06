import flet as ft
import ddbb
import datetime

def main(page: ft.Page):
    page.title = "Registro"

    #def abrir_dialog(message):
        #dialog.content = ft.Text(message)
        #dialog.open = True
        #page.update()


    def cerrar_dialog(e):
        dialog.open = False
        page.update()
    def cerrar_dialog(e):
        dialog.open = False
        page.update()

    def mostrar_mensaje(mensaje):
        print(mensaje)
        dialog.content = ft.Text(mensaje)
        dialog.open = True
        page.update()

    def selecionar_fecha(e):
        fecha_tx.value = f"Fecha: {fecha_dp.value.day}/{fecha_dp.value.month}/{fecha_dp.value.year}"
        page.update()

    contenedor = ft.Container(
        padding=10,
        bgcolor=ft.Colors.BLUE_500,
        width=page.width,
        height=page.height,
    )

    def meter_datos(e):
        nombre = nombre_tf.value
        apellido = apellido_tf.value
        email = email_tf.value
        password = passwd_tf.value
        mensaje = None
        if nombre == "" or nombre is None:
            mensaje = ("Tienes q indicar el nombre")
        elif apellido == "" or apellido is None:
            mensaje = ("Tienes q indicar el apellido")
        elif email == "" or email is None:
            mensaje = ("Tienes q selecionar un email")
        elif password == "" or password is None:
            mensaje = ("Tienes q indicar una contraseña")

        if mensaje is not None:
            mostrar_mensaje(mensaje)
            return

        ddbb.insertar_usuario(nombre, apellido, email, password)
        mostrar_mensaje("USUARIO CREADO")


    def volver(e):
        page.go("/login")
        page.update()

    nombre_tf = ft.TextField(label="Nombre",width=300)
    apellido_tf = ft.TextField(label="Apellidos",width=300)
    email_tf = ft.TextField(label="Email",width=300)
    passwd_tf = ft.TextField(label="Contraseña",width=300)
    datos = ft.FilledButton("Finalizar Registro", on_click= meter_datos)
    #dialog = ft.AlertDialog(modal=True, title=ft.Text("CHE, QUIETO PARAO"), content=ft.Text("Hola"),
                       #actions=[ft.TextButton("Aceptar",on_click=cerrar_dialog),])
    volver_btn = ft.FilledButton(text="Volver al Login",on_click=volver)
    fecha_dp = ft.DatePicker(value=datetime.datetime.now(), on_change=selecionar_fecha)
    fecha_tx = ft.Text(f"Ultimo Login: {fecha_dp.value.day}/{fecha_dp.value.month}/{fecha_dp.value.year}")
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("HEY CHAVAL"),
        actions=[
        ft.TextButton("Aceptar", on_click=cerrar_dialog),
        ]
    )

    columna = ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("REGISTRO"),
            nombre_tf,
            apellido_tf,
            email_tf,
            passwd_tf,
            fecha_tx,
            datos,
            volver_btn,
        ]
    )
    fila = ft.Row(controls=[columna],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    contenedor.content = fila
    #page.overlay.append(dialog)
    page.overlay.append(dialog)
    page.add(contenedor)

    return columna