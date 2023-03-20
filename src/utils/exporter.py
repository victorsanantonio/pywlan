import os
import pandas as pd
from datetime import datetime


class Exporter:
    
    def generate_export_file(self, data, dataset_name):
        generation_time = datetime.utcnow().strftime("%d%m%Y-%H%M%S")
        filename = f"{dataset_name}-{generation_time}.csv"
        self.create_dir()
        pd.DataFrame(data).to_csv(f"data/{filename}", index=False)
        return filename
    
    def confirm_exportation(self, data, dataset_name, confirmation):
        if confirmation == True:
            filename = self.generate_export_file(data, dataset_name)
            print(f"Data exported successfully to {filename}")
    
    def create_dir(self):
        try:
            os.mkdir("data/")
        except OSError:
            pass

exporter = Exporter()