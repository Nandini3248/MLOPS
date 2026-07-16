# sql.py
import os
import pandas as pd
from sql_connection import get_db_connection


class DatabaseQueries:
    def __init__(self):
        self.db = get_db_connection()
        self.employees = []
        self.students = []

        # Load existing data from CSV files if they already exist, otherwise start clean
        if os.path.exists("employee.csv"):
            try:
                df_emp = pd.read_csv("employee.csv")
                df_emp.columns = df_emp.columns.str.strip()
                self.employees = df_emp.to_dict(orient="records")
            except Exception:
                self.employees = []

        if os.path.exists("student.csv"):
            try:
                df_stu = pd.read_csv("student.csv")
                df_stu.columns = df_stu.columns.str.strip()
                self.students = df_stu.to_dict(orient="records")
            except Exception:
                self.students = []

    def save_employee_records(self, emp_dict):
        """Converts raw user input data dictionaries into a structured CSV."""
        df = pd.DataFrame(emp_dict)
        # Ensure column headers match exactly what the ML script expects
        df.columns = ["Employee ID", "Employee Name", "Department", "Employee Salary", "yearsExperience"]
        df.to_csv("employee.csv", index=False)
        self.employees = df.to_dict(orient="records")

    def save_student_records(self, stu_dict):
        """Saves dynamic student collection down to a CSV store."""
        df = pd.DataFrame(stu_dict)
        df.columns = ["Student ID", "Department", "Fee"]
        df.to_csv("student.csv", index=False)
        self.students = df.to_dict(orient="records")

    def fetch_employee_records(self):
        if not self.employees:
            return {"Employee ID": [], "Employee Name": [], "Department": [], "Employee Salary": [],
                    "yearsExperience": []}
        return pd.DataFrame(self.employees).to_dict(orient="list")

    def fetch_student_records(self):
        if not self.students:
            return {"Student ID": [], "Department": [], "Fee": []}
        return pd.DataFrame(self.students).to_dict(orient="list")