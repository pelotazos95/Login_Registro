import psycopg2

def connect():
    conn = psycopg2.connect(
        dbname="sistemas",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    return conn

def obtener_usuarios():
    conn = connect()
    try:
        cursor = conn.cursor()
        query = """SELECT * FROM usuario"""
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
            INSERT INTO usuarios(nombre,apellido,email,passwd)
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

#insertar_usuario("pepe","lopez","pepeL@gmail.com","1234")