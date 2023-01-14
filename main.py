import psycopg2
import json

conn = psycopg2.connect(host='localhost', database='northwind_traders', user='postgres', password='UNloCKed72')
with conn.cursor() as cur:
    with open('suppliers.json') as r_file:
        data = json.load(r_file)
        for i in data:
            cur.execute("INSERT INTO suppliers(company_name, contact_name, country, region, city, phone) VALUES (%s, %s, %s, %s, %s, %s)",
                        (i['company_name'],
                         i['contact'].split(', ')[0],
                         i['address'].split('; ')[0],
                         i['address'].split('; ')[1],
                         i['address'].split('; ')[3],
                         i['phone'])
                        )
            conn.commit()


