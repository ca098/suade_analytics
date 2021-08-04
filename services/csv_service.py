import os
import pandas as pd


class CsvService:
    def __init__(self):
        self.dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
        pass

    def parse_data(self):
        file_type = 'csv'
        seperator = ','
        # dataframe = pd.concat([pd.read_csv(f, sep=seperator) for f in glob.glob(dir_path + "/*." + file_type)],
        #                       ignore_index=True)

        arr = os.listdir(self.dir_path)

        customers = 0
        for file in arr:
            data = pd.read_csv(os.path.join(self.dir_path, file))
            if 'orders' in file:
                customer_orders = data['customer_id'].value_counts()
                items = len(customer_orders)

        return 'test'
