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

        commission_total, prom_one, prom_two, prom_three, prom_four, prom_five = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        for p in promotions_by_date:
            prom_one += p.discounted_amount if p.promotion_id == 1 else 0.0
            prom_two += p.discounted_amount if p.promotion_id == 2 else 0.0
            prom_three += p.discounted_amount if p.promotion_id == 3 else 0.0
            prom_four += p.discounted_amount if p.promotion_id == 4 else 0.0
            prom_five += p.discounted_amount if p.promotion_id == 5 else 0.0

            commission_total += p.discounted_amount

        distinct_orders = {o.order_id for o in promotions_by_date}

        # Running out of time, so did a messy inefficient hack to calculate average order
        avg_order = 0.0
        for i in distinct_orders:
            total = sum(j.total_amount for j in promotions_by_date if j.order_id == i)
            avg_order += total

        avg_order = (avg_order / len(distinct_orders))

        discount_total, order_total, discount_rate_total = 0.0, 0.0, 0.0
        for o in orders_by_date:
            discount_rate_total += o.discount_rate
            discount_total += o.discounted_amount
            order_total += o.total_amount

        discount_rate = round((discount_rate_total / len(orders_by_date)), 2)

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
