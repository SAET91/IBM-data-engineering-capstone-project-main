# Importar las bibliotecas requeridas para conectarse a MySQL
import mysql.connector

# Importar bibliotecas requeridas para conectarse a DB2 o PostgreSql
import psycopg2

# Connectar a MySQL
mysql_connection = mysql.connector.connect(user='root', host='127.0.0.1', database='sales')
mysql_cursor = mysql_connection.cursor()

#PostgreSql
dsn_hostname = '127.0.0.1'
dsn_user = 'postgres'
dsn_pwd = '36582484'
dsn_port = "5432"
dsn_database = 'sales'

# Crear la conexión
pgsql_connection = psycopg2.connect(
    database=dsn_database,
    user=dsn_user,
    password=dsn_pwd,
    host=dsn_hostname,
    port=dsn_port
)

# Crear un cursor
pgsql_cursor = pgsql_connection.cursor()

# Definir la función para obtener el último rowid de PostgreSQL
def get_last_rowid(pgsql_cursor):
    SQL = "SELECT MAX(rowid) FROM sales_data;"
    pgsql_cursor.execute(SQL)
    rowid = pgsql_cursor.fetchone()[0]
    return rowid


# Obtener el último rowid de PostgreSQL
last_rowid_postgresql = get_last_rowid(pgsql_cursor)
print("Last row id on production datawarehouse = ", last_rowid_postgresql)

# Listar todos los registros en la base de datos MySQL con rowid mayor que el de la Data Warehouse
def get_latest_records(cursor, last_rowid_postgresql):
    cursor.execute(f"SELECT * FROM sales_data WHERE rowid > {last_rowid_postgresql}")
    return cursor.fetchall()

# Obtener los nuevos registros de la base de datos MySQL
new_records = get_latest_records(mysql_cursor, last_rowid_postgresql)
print("New rows on staging datawarehouse = ", len(new_records))

# Insertar los registros adicionales de MySQL en PostgreSQL
def insert_records(pgsql_cursor, records):
    for record in records:
        # Insertar registros en la tabla sales_data en PostgreSQL
        pgsql_cursor.execute("INSERT INTO sales_data (rowid, product_id, customer_id,quantity) VALUES (%s, %s, %s, %s)", record)
        
    pgsql_connection.commit()

# Insertar los nuevos registros en PostgreSQL
insert_records(pgsql_cursor, new_records)

print("New rows inserted into production datawarehouse = ", len(new_records))

# Cerrar conexiones
mysql_cursor.close()
mysql_connection.close()
pgsql_cursor.close()
pgsql_connection.close()