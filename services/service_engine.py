from services.csv_service import CsvService


class ServiceEngine(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ServiceEngine, cls).__new__(cls)
            cls._instance.csv_service = CsvService()

        return cls._instance
