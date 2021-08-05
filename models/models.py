class Orders:
    def __init__(self, id, created_at, vendor_id, customer_id):
        self.id = id
        self.created_at = created_at
        self.vendor_id = vendor_id
        self.customer_id = customer_id


class OrderLines:
    def __init__(self, created_at, customer_id, order_id, product_id, product_description, product_price,
                 product_vat_rate, discount_rate,
                 quantity, full_price_amount, discounted_amount, vat_amount, total_amount):
        # Added created at due to it being highly likely to always require this
        self.created_at = created_at
        self.customer_id = customer_id

        self.order_id = order_id
        self.product_id = product_id
        self.product_description = product_description
        self.product_price = product_price
        self.product_vat_rate = product_vat_rate
        self.discount_rate = discount_rate
        self.quantity = quantity
        self.full_price_amount = full_price_amount
        self.discounted_amount = discounted_amount
        self.vat_amount = vat_amount
        self.total_amount = total_amount


class Products:
    def __init__(self, id, description):
        self.id = id
        self.description = description
