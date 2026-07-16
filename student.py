# student.py
import pandas as pd
from sql import DatabaseQueries

class StudentManager:
    def __init__(self, db_queries: DatabaseQueries):
        self.db_queries = db_queries

    def load_student_dataframe(self) -> pd.DataFrame:
        raw_data = self.db_queries.fetch_student_records()
        return pd.DataFrame(raw_data)