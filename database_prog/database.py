import sqlite3 

connection = sqlite3.connect('scalifydata.db')

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS persons (
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    )
""")

cursor.execute("""
    INSERT INTO persons VALUES 
    ('Sam', 'Altman', '36'),
    ('Ilya', 'Sutskever', '38'),
    ('Mira', 'Murati', '30')
""")

connection.commit()

connection.close()