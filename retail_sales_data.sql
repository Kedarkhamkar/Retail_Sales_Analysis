create database retail_sale_db;

use retail_sale_db;

create table sales(
sale_id int primary key auto_increment,
product_name varchar(50) not null,
category varchar(50) not null,
quantity int not null,
price decimal(10,2) not null,
sale_date date not null);

INSERT INTO sales
(product_name, category, quantity, price, sale_date)
VALUES
('Laptop', 'Electronics', 2, 35000, '2026-09-01'),
('Mouse', 'Accessories', 5, 500, '2026-09-02'),
('Keyboard', 'Accessories', 3, 1200, '2026-09-03'),
('Monitor', 'Electronics', 2, 12000, '2026-09-05'),
('Office Chair', 'Furniture', 4, 3500, '2026-09-06'),
('Laptop', 'Electronics', 1, 45000, '2026-09-08'),
('Headphones', 'Accessories', 4, 2500, '2026-09-10'),
('Desk', 'Furniture', 2, 7000, '2026-09-11'),
('Keyboard', 'Accessories', 5, 1200, '2026-09-12'),
('Monitor', 'Electronics', 3, 12000, '2026-09-15');

select * from sales;

-- total revenue

select sum(quantity * price) as "total_revenue" from sales;

-- total transaction   -- for seeing transaction calculate total rows number

select count(*) as "total_transaction" from sales;

-- total revenue according to my category

select category, sum(quantity*price )  from sales group by category;

-- total revenue by product

select product_name, sum(quantity*price) as 'total_revenue_by_product' from sales group by product_name; 

--  highest total rebenue by category

select category, sum(quantity*price ) as "total_revenue"  from sales group by category order by total_revenue desc limit 1 ;

