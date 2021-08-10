from models.models import ProductPromotions


class PromotionsService:
    def __init__(self):
        pass

    def get_commision_figures(self, promotions_by_date: [ProductPromotions]):
        commission_total, prom_one, prom_two, prom_three, prom_four, prom_five = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        for p in promotions_by_date:
            prom_one += p.discounted_amount if p.promotion_id == 1 else 0.0
            prom_two += p.discounted_amount if p.promotion_id == 2 else 0.0
            prom_three += p.discounted_amount if p.promotion_id == 3 else 0.0
            prom_four += p.discounted_amount if p.promotion_id == 4 else 0.0
            prom_five += p.discounted_amount if p.promotion_id == 5 else 0.0

            commission_total += p.discounted_amount

        return commission_total, prom_one, prom_two, prom_three, prom_four, prom_five

    def get_average_order_amount(self, promotions_by_date: [ProductPromotions]) -> float:
        distinct_orders = {o.order_id for o in promotions_by_date}

        avg_order = 0.0
        for i in distinct_orders:
            total = sum(j.total_amount for j in promotions_by_date if j.order_id == i)
            avg_order += total

        return avg_order / len(distinct_orders)
