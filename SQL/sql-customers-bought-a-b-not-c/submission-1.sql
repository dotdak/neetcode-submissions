-- Write your query below
select * from customers
where customer_id not in (
    select customer_id from orders
    where product_name = 'C'
) and customer_id in (
    select customer_id from orders
    where product_name = 'A' 
) and customer_id in (
    select customer_id from orders
    where product_name = 'B' 
)
order by customer_name