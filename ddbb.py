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

def insertar_usuario(v_nombre,v_apellido,v_email,v_contraseña):
    conn = connect()

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO usuarios(nombre,apellido,email,contraseña)
            VALUES(%s,%s,%s,%s)
            """
        cursor.execute(query, (v_nombre,v_apellido,v_email,v_contraseña))
        conn.commit()
        print("Usuario insertado correctamente")
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()

#insertar_usuario("pepe","lopez","pepeL@gmail.com","1234")