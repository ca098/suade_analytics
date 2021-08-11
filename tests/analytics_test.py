import unittest

from services.service_engine import ServiceEngine

SE = ServiceEngine()

order_lines = SE.csv_service.read_csv('order_lines.csv')
orders = SE.csv_service.read_csv('orders.csv')
product_promotions = SE.csv_service.read_csv('product_promotions.csv')


class AnalyticsTest(unittest.TestCase):

    def test_orders_by_date(self):
        date = '2019-08-01'

        f_date = '"{}"'.format(date)
        orders_by_date = SE.query_service.get_orders_for_date(order_lines=order_lines, orders=orders, date=f_date)
        distinct_orders = len({o.order_id for o in orders_by_date})

        self.assertTrue(distinct_orders, 9)

    def test_items_by_date(self):
        self.assertTrue(True, True)
