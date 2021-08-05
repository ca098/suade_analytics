from flasgger import swag_from
from flask import Blueprint, jsonify
import re

from services.service_engine import ServiceEngine

ANALYTICS_BLUEPRINT = Blueprint('analytics_blueprint', __name__)

SE = ServiceEngine()


@ANALYTICS_BLUEPRINT.route('/get_analytics_report/<string:date>', methods=['GET'])
@swag_from('swagger/get_analytics_report.yml')
def get_analytics_report(date):
    valid_str = re.match(r'^20[0-2][0-9]-((0[1-9])|(1[0-2]))-([0-2][1-9]|3[0-1])$', date)

    if valid_str:
        order_lines = SE.csv_service.read_csv('order_lines.csv')
        orders = SE.csv_service.read_csv('orders.csv')
        orders_by_date = SE.query_service.get_orders_for_date(order_lines, orders, date)

        items_sold = len(orders_by_date)

        # TODO - Make this more efficient (1 loop)
        customer_orders = len({o.customer_id for o in orders_by_date})
        discount_total = round(sum(o.discounted_amount for o in orders_by_date), 2)
        order_total = round(sum(o.total_amount for o in orders_by_date), 2)

        payload = {
            'customers': customer_orders,
            'total_discount_amount': discount_total,
            'items': items_sold,
            'order_total_avg': order_total

        }

        return jsonify(payload)

    else:
        return jsonify({'message': 'Incorrect string format. Please ensure it is in the YYYY-MM-DD format'}), 400
