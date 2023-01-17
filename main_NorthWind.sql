--Создание таблицы для заполнения информации о поставщиках
CREATE TABLE suppliers
(
	supplier_id serial PRIMARY KEY,
	company_name varchar(150) NOT NULL, 
	contact_name varchar (150),
	country varchar (150),
	region varchar (150),
	city varchar (150),
	phone varchar (150)
)

--Добавление столбца с id поставщика в таблицу продуктов. 
ALTER TABLE products ADD COLUMN supplier_id int
ALTER TABLE products ADD CONSTRAINT fk_products_supplier_id FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
