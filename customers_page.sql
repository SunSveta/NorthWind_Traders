select * from customers

--Количество заказчиков
SELECT COUNT (*) FROM customers

--Уникальные сочетания городов и стран, в которых зарегистрированы заказчики
SELECT DISTINCT country, city FROM customers
ORDER BY country, city  --для удобства отображения

--Название компании заказчика и ФИО обрабатывающего сотрудника, оба из Лондона, доставка ведется компанией Speedy Express
SELECT DISTINCT customers.company_name, CONCAT(first_name, ' ', last_name) AS emp_fio
FROM customers 
INNER JOIN employees AS e USING(city)
INNER JOIN orders AS o USING(customer_id)
INNER JOIN shippers AS s ON o.ship_via=s.shipper_id
WHERE city='London' AND s.company_name='Speedy Express'

--Заказчики, не сделавшие ни одного заказа. Вывести имя заказчика и order_id.
SELECT customers.contact_name, orders.order_id
FROM customers
FULL JOIN orders USING(customer_id)
WHERE orders.customer_id IS NULL



