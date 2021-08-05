from services.csv_service import CsvService
from services.query_service import QueryService


class ServiceEngine(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ServiceEngine, cls).__new__(cls)
            cls._instance.csv_service = CsvService()
            cls._instance.query_service = QueryService()

        return cls._instance
