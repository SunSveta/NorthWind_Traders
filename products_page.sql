--Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, 
--которых в продаже менее 20 единиц. Вывести наименование продуктов, кол-во единиц в продаже, 
--имя контакта поставщика и его телефонный номер.
SELECT prod.product_name, prod.units_in_stock, s.contact_name, s.phone
FROM products AS prod
JOIN suppliers AS s USING (supplier_id)
JOIN categories AS cat USING(category_id)
WHERE prod.discontinued=0 AND prod.units_in_stock < 20 AND cat.category_name IN('Beverages', 'Seafood')