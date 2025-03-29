import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Navegacion"

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
        minutos = minutos_drop.value
        hora = horas_drop.value
        dia = dias_drop.value
        mes = mes_drop.value
        evento = evento_tf.value
        print(f'Minutos: {minutos}, Hora: {hora}, Dia: {dia}, Mes: {mes}, Evento: {evento}')
        if minutos is None:
            abrir_dialog("Tienes q selecionar minutos")
            return
        elif hora is None:
            abrir_dialog("Tienes q selecionar horas")
            return
        elif evento == "":
            abrir_dialog("Tienes q selecionar eventos")
            return

    def obtener_minutos():
        # Crear lista vacia
        lista_minutos = []
        for i in range(1,60):
            minutos_str = str(i).zfill(2)
            opcion = ft.dropdown.Option(text=minutos_str, key=minutos_str)
            lista_minutos.append(opcion)
        return lista_minutos
    def obtener_horas():
        # Crear lista vacia
        lista_horas = []
        for i in range(0,24):
            horas_str = str(i).zfill(2)
            opcion = ft.dropdown.Option(text=horas_str, key=horas_str)
            lista_horas.append(opcion)
        return lista_horas
    def obtener_dias():
        # Crear lista vacia
        lista_dias = []
        for i in range(1,32):
            dias_str = str(i)
            opcion = ft.dropdown.Option(text=dias_str, key=dias_str)
            lista_dias.append(opcion)
        return lista_dias
    def obtener_mes():
        # Crear lista vacia
        lista_mes = []
        for i in range(1,13):
            mes_str = str(i)
            opcion = ft.dropdown.Option(text=mes_str, key=mes_str)
            lista_mes.append(opcion)
        return lista_mes

    contenedor = ft.Container(
        padding=10,
        bgcolor=ft.Colors.BLUE_500,
        width=page.width,
        height=page.height,
    )

    def volver(e):
        page.go("/loginPage")

    minutos_tf = ft.TextField(label="Minutos")
    minutos_drop = ft.Dropdown(label="Minutos",options=obtener_minutos(),width=300)
    horas_tf = ft.TextField(label="Horas")
    horas_drop = ft.Dropdown(label="Horas",options=obtener_horas(),width=300)
    dias_tf = ft.TextField(label="Dias")
    dias_drop = ft.Dropdown(label="Dias",options=obtener_dias(),width=300)
    mes_tf = ft.TextField(label="Mes")
    mes_drop = ft.Dropdown(label="Mes",options=obtener_mes(),width=300)
    evento_tf = ft.TextField(label="Evento",width=300)
    fecha_dp = ft.DatePicker(value=datetime.datetime.now(), on_change=selecionar_fecha)
    fecha_tx = ft.Text(f"Fecha: {fecha_dp.value.day}/{fecha_dp.value.month}/{fecha_dp.value.year}")
    boton_fecha = ft.ElevatedButton("Seleciona la fecha",on_click=abrir_selector)
    dialog = ft.AlertDialog(modal=True, title=ft.Text("Informacion"), content=ft.Text("Hola"),
                       actions=[ft.TextButton("Aceptar",on_click=cerrar_dialog),])
    volver_btn = ft.ElevatedButton(text="Volver",on_click=volver)

    columna = ft.Column(
        alignment=ft.CrossAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Programador de Tareas"),
            minutos_drop,
            horas_drop,
            #dias_drop,
            #mes_drop,
            fecha_tx,
            boton_fecha,
            evento_tf,
            ft.ElevatedButton("Crear Tarea", on_click=obtener_valores),
            volver_btn,
        ]
    )
    fila = ft.Row(controls=[columna],
        alignment=ft.MainAxisAlignment.CENTER,
    )




    contenedor.content = fila
    page.overlay.append(fecha_dp)
    page.overlay.append(dialog)
    page.add(contenedor)

    return columna


#ft.app(target=main, view=ft.WEB_BROWSER)
