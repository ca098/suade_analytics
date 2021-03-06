GET_ORDERS_BY_DATE_QUERY = "SELECT o.created_at, o.customer_id, ol.* from orders o inner join order_lines ol on o.id = ol.order_id where date(o.created_at) = {}"

GET_PROMOTIONS_BY_DATE_QUERY = "SELECT o.created_at, po.promotion_id, ol.* from product_promotions po inner join order_lines ol on po.product_id = ol.product_id inner join orders o on o.id = ol.order_id where date(o.created_at) = {}"