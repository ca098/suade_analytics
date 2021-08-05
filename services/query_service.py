import pandasql as ps
from models.models import *

from queries.queries import GET_ORDERS_BY_DATE_QUERY


class QueryService:
    def __init__(self):
        pass

    def get_orders_for_date(self, order_lines, orders, date) -> [OrderLines]:
        date = '"{}"'.format(date)
        order_line_df = ps.sqldf(GET_ORDERS_BY_DATE_QUERY.format(date))

        order_lines_list = []
        for idx, row in order_line_df.iterrows():
            order_line = OrderLines(row['created_at'], row['customer_id'], row['order_id'], row['product_id'], row['product_description'],
                                    row['product_price'], row['product_vat_rate'], row['discount_rate'],
                                    row['quantity'], row['full_price_amount'], row['discounted_amount'],
                                    row['vat_amount'], row['total_amount'])
            order_lines_list.append(order_line)

        return order_lines_list
