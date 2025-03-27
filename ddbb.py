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

def comprobar_usuario(v_email,v_passwd):
    conn = connect()

    try:
        cursor = conn.cursor()
        query = """
            select * from usuarios
            where email = %s
            and passwd = %s;
            """
        if v_email != obtener_usuarios().email and v_passwd != obtener_usuarios().passwd:
            print("Usuario no existe")
        else:
            cursor.execute(query, (v_email,v_passwd))

    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            cursor.close()
            conn.close()


#insertar_usuario("pepe","lopez","pepeL@gmail.com","1234")