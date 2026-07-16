
from sql import DatabaseQueries
from employee import EmployeeManager
from student import StudentManager
from finance_analysis import FinanceAnalyzer


def get_runtime_inputs():
    db_queries = DatabaseQueries()
    valid_departments = {"CSE", "ECE", "EEE"}


    print("--- STEP A: INPUT EMPLOYEE DATA ---")
    emp_dict = {"Employee_ID": [], "Department": [], "Salary_Expense": [], "Mentor_Capacity": []}
    emp_count = int(input("How many employees would you like to add? "))

    for i in range(emp_count):
        print(f"\nRecording data for Employee #{i + 1}:")
        emp_id = int(input("  Enter Employee ID (e.g., 101): "))

        dept = ""
        while dept not in valid_departments:
            dept = input("  Enter Department (CSE, ECE, EEE): ").strip().upper()
            if dept not in valid_departments:
                print("  [Error] Invalid choice. Must type CSE, ECE, or EEE.")

        salary = float(input("  Enter Monthly Salary Cost (₹): "))
        capacity = int(input("  Enter Mentor Student Capacity Max limit: "))

        emp_dict["Employee_ID"].append(emp_id)
        emp_dict["Department"].append(dept)
        emp_dict["Salary_Expense"].append(salary)
        emp_dict["Mentor_Capacity"].append(capacity)

    db_queries.save_employee_records(emp_dict)


    print("\n--- STEP B: INPUT STUDENT DATA ---")
    stu_dict = {"Student_ID": [], "Department": [], "Fee": []}
    stu_count = int(input("How many students would you like to add? "))

    for i in range(stu_count):
        print(f"\nRecording data for Student #{i + 1}:")
        stu_id = int(input("  Enter Student ID (e.g., 201): "))

        dept = ""
        while dept not in valid_departments:
            dept = input("  Enter Department (CSE, ECE, EEE): ").strip().upper()
            if dept not in valid_departments:
                print("  [Error] Invalid choice. Must type CSE, ECE, or EEE.")

        fee = float(input("  Enter Course Fee Revenue Received (₹): "))

        stu_dict["Student_ID"].append(stu_id)
        stu_dict["Department"].append(dept)
        stu_dict["Fee"].append(fee)

    db_queries.save_student_records(stu_dict)
    return db_queries


def main():
    print("==================================================================")
    print("      DEPARTMENT FINANCIAL & CAPACITY RESOURCE ANALYSIS ENGINE     ")
    print("==================================================================\n")


    db_backend = get_runtime_inputs()


    emp_manager = EmployeeManager(db_backend)
    stu_manager = StudentManager(db_backend)

    df_employees = emp_manager.load_employee_dataframe()
    df_students = stu_manager.load_student_dataframe()

    print("\nAnalyzing Submitted Data Matrix...")
    analyzer = FinanceAnalyzer(df_employees, df_students)
    summary_report = analyzer.process_metrics()


    print("\n============================ DEPARTMENT-WISE ANALYSIS ============================")
    if not summary_report.empty:
        print(summary_report[
                  ["Student_Count", "Total_Capacity", "Capacity_Utilization_Pct", "Profit_Loss", "Suggestion"]])
    else:
        print("No valid overlapping department entries were captured.")
    print("==================================================================================\n")


    output_img = "department_profit_loss_chart.png"
    analyzer.generate_report_chart(output_img)
    print(f"Workflow complete! Graphic dashboard updated and exported to '{output_img}'.")


if __name__ == "__main__":
    main()