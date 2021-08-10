from flasgger import swag_from
from flask import Blueprint, jsonify
import re

from services.service_engine import ServiceEngine

ANALYTICS_BLUEPRINT = Blueprint('analytics_blueprint', __name__)

SE = ServiceEngine()


@ANALYTICS_BLUEPRINT.route('/get_analytics_report/<string:date>', methods=['GET'])
@swag_from('swagger/get_analytics_report.yml')
def get_analytics_report(date):
    valid_str = re.match(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$', date)

    if valid_str:
        order_lines = SE.csv_service.read_csv('order_lines.csv')
        orders = SE.csv_service.read_csv('orders.csv')
        product_promotions = SE.csv_service.read_csv('product_promotions.csv')

        f_date = '"{}"'.format(date)

        orders_by_date = SE.query_service.get_orders_for_date(order_lines, orders, f_date)
        promotions_by_date = SE.query_service.get_promotions_for_date(product_promotions, order_lines, orders, f_date)

        if len(orders_by_date) == 0 or len(promotions_by_date) == 0:
            return jsonify({f'message': f'No data for date: {date}'}), 200

        items_sold = sum(o.quantity for o in orders_by_date)
        customer_orders = len({o.customer_id for o in orders_by_date})

        commission_total, prom_one, prom_two, prom_three, prom_four, prom_five = SE.promotions_service.get_commision_figures(promotions_by_date)

        # Running out of time, so did a messy inefficient hack to calculate average order
        avg_order = SE.promotions_service.get_average_order_amount(promotions_by_date)

        discount_total, order_total, discount_rate = SE.order_lines_service.get_discount_orders(orders_by_date)

        promotions = {
            "1": round(prom_one, 2),
            "2": round(prom_two, 2),
            "3": round(prom_three, 2),
            "4": round(prom_four, 2),
            "5": round(prom_five, 2),
        }

        commissions = {'promotions': promotions,
                       'total': round(commission_total, 2),
                       'order_average': round(avg_order, 2)}

        payload = {
            'customers': customer_orders,
            'total_discount_amount': round(discount_total, 2),
            'items': items_sold,
            'order_total_avg': round(order_total, 2),
            'discount_rate_avg': discount_rate,
            'commissions': commissions

        }

        return jsonify(payload), 200

    else:
        return jsonify({'message': 'Incorrect string format. Please ensure it is in the YYYY-MM-DD format'}), 400
