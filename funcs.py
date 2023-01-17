import psycopg2

config = {'host': 'localhost', 'database': 'northwind_traders', 'user': 'postgres', 'password': '*******'}

def get_product_by_id(config, id):
    with psycopg2.connect(
            host=config.get('host'),
            database=config.get('database'),
            user=config.get('user'),
            password=config.get('password')
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT product_id, product_name, category_name, unit_price FROM products JOIN categories USING(category_id) WHERE product_id = {id}")
            result = cur.fetchall()
            for i in result:
                print(f"id: {i[0]}; Название: {i[1]}; Категория: {i[2]}; Цена: {i[3]} каких-то денег.")


def get_category_by_id(config, id):
    with psycopg2.connect(
            host=config.get('host'),
            database=config.get('database'),
            user=config.get('user'),
            password=config.get('password')
    ) as conn:
        with conn.cursor() as cur:
            prod_list = list()
            cur.execute(
                f"SELECT category_id, category_name, description, product_name FROM categories JOIN products USING(category_id) WHERE category_id = {id}")
            result = cur.fetchall()
            for i in result:
                prod_list.append(i[3])
            print(f"id категории: {i[0]}; Название категории: {i[1]}; Описание: {i[2]}; Продукты из этой категории: {prod_list}.")


get_product_by_id(config, 65)
get_category_by_id(config, 6)