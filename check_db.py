import sqlite3
"""Corre este modulo para ver si una tabla existe en tu sqlite
    En este caso verificamos por user que la unica table creada en este ejemplo
"""

conn = sqlite3.connect('instance/your_database_name.db')
cursor = conn.cursor()

table_name = 'user'
#Ejecuta commando de sql para encontrar la tabla
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")

# verificamos si encontramos algo con el commando aterior
result = cursor.fetchone()
if result:
    print(f"Table '{table_name}' exists.")
else:
    print(f"Table '{table_name}' does not exist.")

conn.close() # cerramos la connecion con la base de datos
