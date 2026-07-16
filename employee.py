# employee.py
import pandas as pd
from sql import DatabaseQueries

class EmployeeManager:
    def __init__(self, db_queries: DatabaseQueries):
        self.db_queries = db_queries

    def load_employee_dataframe(self) -> pd.DataFrame:
        raw_data = self.db_queries.fetch_employee_records()
        return pd.DataFrame(raw_data)