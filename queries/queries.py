GET_ORDERS_BY_DATE_QUERY = "SELECT o.created_at, o.customer_id, ol.* from orders o inner join order_lines ol on o.id = ol.order_id where date(o.created_at) = {}"