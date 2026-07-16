# finance_analysis.py
import pandas as pd
import matplotlib.pyplot as plt


class FinanceAnalyzer:
    def __init__(self, employee_df: pd.DataFrame, student_df: pd.DataFrame):
        self.employee_df = employee_df
        self.student_df = student_df
        self.summary_df = None

    def process_metrics(self):
        if self.employee_df.empty or self.student_df.empty:
            self.summary_df = pd.DataFrame()
            return self.summary_df

        dept_employees = self.employee_df.groupby("Department").agg(
            Total_Expense=("Salary_Expense", "sum"),
            Total_Capacity=("Mentor_Capacity", "sum"),
            Employee_Count=("Employee_ID", "count")
        )

        dept_students = self.student_df.groupby("Department").agg(
            Total_Revenue=("Fee", "sum"),
            Student_Count=("Student_ID", "count")
        )

        merged = pd.merge(dept_employees, dept_students, on="Department", how="outer").fillna(0)
        merged["Profit_Loss"] = merged["Total_Revenue"] - merged["Total_Expense"]

        merged["Capacity_Utilization_Pct"] = merged.apply(
            lambda r: (r["Student_Count"] / r["Total_Capacity"] * 100) if r["Total_Capacity"] > 0 else 0.0, axis=1
        )
        merged["Students_per_Mentor"] = merged.apply(
            lambda r: (r["Student_Count"] / r["Employee_Count"]) if r["Employee_Count"] > 0 else 0.0, axis=1
        )

        merged["Suggestion"] = merged["Capacity_Utilization_Pct"].apply(
            lambda x: "Add more employees" if x > 80 else "No requirement"
        )

        available_depts = [d for d in ["CSE", "ECE", "EEE"] if d in merged.index]
        self.summary_df = merged.reindex(available_depts)
        return self.summary_df

    def generate_report_chart(self, filename="department_profit_loss_chart.png"):
        if self.summary_df is None or self.summary_df.empty:
            print("[System Alert] Not enough dynamic calculation metrics data to build the chart layout.")
            return

        color_map = {"CSE": "red", "ECE": "blue", "EEE": "yellow"}
        colors = [color_map.get(dept, "gray") for dept in self.summary_df.index]

        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar(self.summary_df.index, self.summary_df["Profit_Loss"], color=colors, edgecolor='black', width=0.4)

        ax.axhline(0, color='black', linewidth=1)
        ax.set_title("Department-wise Profit / Loss Analysis", fontsize=14, pad=15)
        ax.set_xlabel("Departments", fontsize=12)
        ax.set_ylabel("Profit / Loss (₹)", fontsize=12)
        ax.grid(axis='y', linestyle='--', alpha=0.5)

        for bar in bars:
            yval = bar.get_height()
            va_dir = 'bottom' if yval >= 0 else 'top'
            xy_text_dir = (0, 5) if yval >= 0 else (0, -12)

            ax.annotate(f"₹{int(yval):,}",
                        xy=(bar.get_x() + bar.get_width() / 2, yval),
                        xytext=xy_text_dir,
                        textcoords="offset points",
                        ha='center', va=va_dir, fontsize=10, fontweight='bold')

        plt.tight_layout()
        plt.savefig(filename)
        plt.show()
        plt.close()