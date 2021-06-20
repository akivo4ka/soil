import pandas as pd
import psycopg2

path = "soil-main\\tables_descript.xlsx"
table_names = pd.read_excel(path, header=None).values
QUERY = "CREATE TABLE {} (ID serial PRIMARY KEY, {});"
queries = {}
for table_name in table_names:
    name = str(table_name[0])
    df = pd.read_excel(path, sheet_name=name, header=None)
    q = ""
    for v in df.values:
        v[0] = "NA" if isinstance(v[0], float) else v[0]
        q += "{} {}, ".format(*v)
    queries[name] = QUERY.format(name, q[:-2])

for name, query in queries.items():
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
        cur.execute(query)
        conn.commit()
        print("{} SUCCESS".format(name))
    except BaseException as e:
        print("{} FAIL\nQUERY:\n{}".format(name, query))
        print(str(e))
    finally:
        cur.close()
        conn.close()
