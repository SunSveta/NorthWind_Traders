import psycopg2
import json

conn = psycopg2.connect(host='localhost', database='northwind_traders', user='postgres', password='*******')
with conn.cursor() as cur:
    result_products_lst = {}
    with open('suppliers.json') as r_file:
        data = json.load(r_file)
        for i in data:
            cur.execute("INSERT INTO suppliers(company_name, contact_name, country, region, city, phone) VALUES (%s, %s, %s, %s, %s, %s) RETURNING supplier_id",
                        (i['company_name'],
                         i['contact'].split(', ')[0],
                         i['address'].split('; ')[0],
                         i['address'].split('; ')[1],
                         i['address'].split('; ')[3],
                         i['phone'])
                        )
            sup_id = cur.fetchone()[0]

            for j in i.get('products'):
                result_products_lst.update({j:sup_id})
        big_sql_row = ''
        for k, v in result_products_lst.items():
            prod_name = k
            name = prod_name.replace("'", "''")
            big_sql_row += f"UPDATE products SET supplier_id = {v} WHERE product_name = '{name}'; "
        cur.execute(big_sql_row)
        conn.commit()



