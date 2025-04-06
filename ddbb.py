import psycopg2
import loginPage


def connect():
    conn = psycopg2.connect(
        dbname="basedatos_e",
        user="postgres",
        password="51_dam56",
        host="localhost",
        port="4445"
    )
    return conn

def obtener_usuarios():
    conn = connect()
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM usuarios"""
        cursor.execute(query)
        usuario = cursor.fetchall()
        print(usuario)
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            cursor.close()
            conn.close()
    return usuario

def insertar_usuario(v_nombre,v_apellido,v_email,v_passwd):
    conn = connect()

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO usuarios(nombre,apellidos,email,passwd)
            VALUES(%s,%s,%s,%s)
            """
        cursor.execute(query, (v_nombre,v_apellido,v_email,v_passwd))
        conn.commit()
        print("Usuario insertado correctamente")
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()

def comprobar_usuario(v_email,v_passwd):
    conn = connect()

    try:
        cursor = conn.cursor()
        query = """
            select email,passwd from usuarios
            where email = %s AND passwd = %s;
            """
        cursor.execute(query, (v_email, v_passwd))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Usuario no existe")
            conn.close()
        else:
            print("USUARIO CORRECTO")
            loginPage.volver_infoPage()

    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            cursor.close()
            conn.close()


#insertar_usuario("pepe","lopez","pepeL@gmail.com","1234")