# Write your MySQL query statement below
select
    Product.product_id,
    product_name
from Product
    right join Sales on Sales.product_id = Product.product_id
group by Sales.product_id
having
    min(Sales.sale_date) >= '2019-01-01'
    and max(Sales.sale_date) <= '2019-03-31'