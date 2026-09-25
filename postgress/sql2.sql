select concat('Monisha',' ','Maruthaiyan');

select * from students;
-- Rian22S001
select concat(name,'-',age) from students where age is null;
-- concat with seperator
select concat_ws(',',name,age) from students where age is null;

select count(age) from students;

select substring(to_char(joined,'yyyy-mm-dd'),1,4) from students;
select city,substring(city,length(city)-4) from students;



-- Aggregate Function
select max(age),min(age) from students;



-- single row Subquery
-- we can use camparision Operator to connect with outer query
select * from students where age = (select min(age) from students);
select * from students where age=30;

/* single row subquery 
1. Find the orders where the total amount is greater than the average order amount.
2. Find the product with the highest price.

2. Multiple row subquery
Find the customers who have placed more than one order.
Find the products whose price is greater than the price of any product in the Electronics category.

3.Multiple Column subquery
Find the products that have the same category and price as another product.
Find the orders that have the same customer and order status as another order.

corelated:
Find the customers who have placed at least one order.
Find the products whose price is greater than the average price of products in the same category.

non-corelated:
Find the products whose price is greater than the average product price.
Find the orders whose total amount is greater than the highest order amount of customer 5.

Select Clause:
Display each product name along with the average product price.
Display each order along with the highest order amount.

from clause:
Find the average order amount for each customer using a subquery in the FROM clause.
Find the total sales for each product using a subquery in the FROM clause.

where Clause:
-------------
Find the products whose price is greater than the average product price.
Find the orders placed by customers from Chennai.


in: Find customers who have placed an order.
any: Find products whose price is greater than any product in the Electronics category.
all: Find products whose price is greater than all products in the Electronics category.
exists: Find customers who have placed at least one order.
*/

select * from orders 
where total_amount>=(select round(avg(total_amount)) from orders);
select * from products where price=(select max(price) from products);

select * from orders where customer_id in(
select customer_id 
from orders 
group by customer_id 
having count(customer_id)>1);


select * from products where price> any(
select price from products where category='Electronics');
select * from products where (category,price) in
(select category,price from products group by category,price having count(*)>1);

select * from orders where (customer_id,status) in 
(select customer_id,status from orders group by customer_id,status having count(*)>1);


-- corelated 
-- exists

select * from customers;
select * from orders;

select * from customers c where exists 
(select * from orders o where o.customer_id = c.customer_id );

SELECT c.customer_id, c.customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1 
    FROM orders o 
    WHERE o.customer_id = c.customer_id
);

select product_name,price,(select round(avg(price),2) from products) from products;

-- select () from table_name;
-- select * from () ; 
-- select * from where () ;

select customer_id,round(avg(total_amount))
from (select customer_id,total_amount from orders) as o group by customer_id;


select * from products where price>=(select avg(price) from products);