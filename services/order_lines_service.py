class OrderLinesService:
    def __init__(self):
        pass

    def get_discount_orders(self, orders_by_date):
        discount_total, order_total, discount_rate_total = 0.0, 0.0, 0.0
        for o in orders_by_date:
            discount_rate_total += o.discount_rate
            discount_total += o.discounted_amount
            order_total += o.total_amount

        discount_rate = round((discount_rate_total / len(orders_by_date)), 2)

        return discount_total, order_total, discount_rate

