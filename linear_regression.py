# linear_regression.py
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def run_csv_regression(csv_filename="employee.csv"):
    if not os.path.exists(csv_filename):
        print(f"[Error] '{csv_filename}' not found. Cannot run regression computation model pipeline.")
        return

    try:
        # Load the newly saved data frame from the file
        df = pd.read_csv(csv_filename)
        df.columns = df.columns.str.strip()

        if len(df) < 2:
            print("\n[Warning] Need at least 2 rows of employee rows in your CSV file to derive a linear model.")
            return

        # Feature matrix extraction using the precise runtime columns
        x = df[['yearsExperience']]
        y = df['Employee Salary']

        model = LinearRegression()
        model.fit(x, y)
        y_pred = model.predict(x)

        print("\n=================== REGRESSION MODEL METRICS ===================")
        print(f"Intercept: ₹{model.intercept_:,.0f}")
        print(f"Slope: ₹{model.coef_[0]:,.0f}/yr")
        print(f"R^2 Score: {r2_score(y, y_pred):.3f}")
        print(f"RMSE: ₹{np.sqrt(mean_squared_error(y, y_pred)):,.0f}")
        print("================================================================\n")

        # Render the custom graphical analysis
        plt.figure(figsize=(8, 5))
        plt.scatter(x, y, color='blue', label='User Inputs (from CSV)', s=80, zorder=5)
        plt.plot(df['yearsExperience'], y_pred, color='red', linewidth=2, label='Linear Regression Line')

        plt.title("Salary Forecast Model via Recorded CSV Experience Metrics", fontsize=11, pad=12)
        plt.xlabel("Years of Experience", fontsize=10)
        plt.ylabel("Employee Salary (₹)", fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        plt.tight_layout()

        print("Displaying predictive best fit trend line...")
        plt.show()

    except Exception as e:
        print(f"[Error] Regression step failed: {e}")