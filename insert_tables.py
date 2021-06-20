import psycopg2
import pandas as pd
import numpy as np

names = [
    'SOIL_SEM',
    'SOIL_MAIN_HORIZONS',
    'SOIL_ADD_HORIZONS',
    'SOIL_MORPH',
    'SOIL_MORPH_ELEM',
    'SOIL_CHEM',
    'SOIL_PHYS',
    'SOIL_MAP_LEGEND',
    'SOIL_MAP_PARENT_LEGEND',
    'SOIL_MAP',
    'SOIL_DATA'
]


QUERY = """INSERT INTO {} ({}) VALUES ({})"""

def nan_to_null(f, _NULL=psycopg2.extensions.AsIs('NULL'), _Float=psycopg2.extensions.Float):
    if not np.isnan(f):
        return _Float(f)
    return _NULL

psycopg2.extensions.register_adapter(float, nan_to_null)

for name in names:
    file = "soil-main\\{}.xlsx".format(name.lower())
    df = pd.read_excel(file)
    joined_columns = ', '.join(df.columns)
    number_of_columns = len(df.columns)
    joined_s = ', '.join(['%s'] * number_of_columns)
    query = QUERY.format(name, joined_columns, joined_s)
    values = df.values
    try:
        conn = psycopg2.connect("""
            host=rc1a-6fz5ned1qx1wmx9o.mdb.yandexcloud.net
            port=6432
            dbname=agro
            user=dev
            password=H@v3-@-n1c3_daY!
            target_session_attrs=read-write
            sslmode=verify-full
        """)
        cur = conn.cursor()
        cur.executemany(query, values)
        conn.commit()
        print("{} SUCCESS".format(name))
    except:
        print("{} FAIL".format(name))
        print(query)
    finally:
        cur.close()
        conn.close()
