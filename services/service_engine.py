from services.csv_service import CsvService
from services.order_lines_service import OrderLinesService
from services.promotions_service import PromotionsService
from services.query_service import QueryService


class ServiceEngine(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ServiceEngine, cls).__new__(cls)
            cls._instance.csv_service = CsvService()
            cls._instance.query_service = QueryService()
            cls._instance.promotions_service = PromotionsService()
            cls._instance.order_lines_service = OrderLinesService()

        return cls._instance
