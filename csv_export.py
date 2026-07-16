#from _pyrepl import reader

#import employee

#data=employee.view_employee()
#print(data)


#read -r
#write() -w
#append - a
#file("File_name",mode)
#file.close()
#with open("employee.txt","r") as db:
import csv
import employee

def csv_convert():
    print("CSV Export Started")

    employees = employee.view_employee()

    if employees is None:
        print("No employee data")
        return

    if len(employees) == 0:
        print("No employees found")
        return

    with open("employees.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
            "Employee ID",
            "Employee Name",
            "Department",
            "Employee Salary"
        ])

        for emp in employees:
            writer.writerow([
                emp[0],
                emp[1],
                emp[2],
                emp[3],

            ])

    print("\nEmployee data successfully exported")


if __name__ == "__main__":
    csv_convert()