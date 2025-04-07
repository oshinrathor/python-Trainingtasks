from datetime import date, timedelta, datetime  # Ensure correct import

class Employee:
    """Manages the employee attendance records"""

    employee_list = []  # List to hold all employee records

    def create_employee(self, name, age):
        # Generating employee ID dynamically by incrementing based on the length of employee list
        emp_id = len(self.employee_list) + 1001
        employee = {
            'Emp_id': emp_id,
            'name': name,
            'age': age,
            'attendance': {}  # Adding an empty dictionary for attendance records
        }
        print(f"Employee created successfully, employee id: {emp_id}")
        self.employee_list.append(employee)

    def display_employee_all(self):
        if not self.employee_list:
            print("No employees found.")
            return
        for employee in self.employee_list:
            print(f"Emp_id: {employee['Emp_id']}, Name: {employee['name']}, Age: {employee['age']}")

    def mark_attendance(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                # Create a dictionary to store attendance data with date as key and status as value
                emp_attendance = {}
                last_seven_date = date.today() - timedelta(days=7)
                for i in range(7):  # Loop for the last 7 days
                    attendance_date = last_seven_date + timedelta(days=i)
                    status = input(f"Enter attendance for {attendance_date}: 'p' for present, 'a' for absent: ")
                    # Store attendance status for each day
                    emp_attendance[attendance_date] = status
                employee['attendance'] = emp_attendance
                print(f"Attendance marked for Employee ID: {emp_id}")
                return
        print(f"Employee with ID {emp_id} not found.")

    def view_attendance(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                if employee['attendance']:
                    print(f"Attendance for Employee ID {emp_id}:")
                    for date, status in employee['attendance'].items():
                        print(f"{date}: {status}")
                else:
                    print(f"No attendance recorded for Employee ID {emp_id}")
                return
        print(f"Employee with ID {emp_id} not found.")

    def modify_attendance(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                if not employee['attendance']:
                    print(f"No attendance to modify for Employee ID {emp_id}.")
                    return

                print(f"Modify attendance for Employee ID {emp_id}:")
                for date in employee['attendance'].keys():
                    print(f"{date}: {employee['attendance'][date]}")

                date_to_modify_str = input("Enter the date (YYYY-MM-DD) to modify attendance: ")
                
                # Convert user input to a datetime.date object
                try:
                    # Correct the line here
                    date_to_modify = datetime.strptime(date_to_modify_str, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    return
                
                if date_to_modify in employee['attendance']:
                    current_status = employee['attendance'][date_to_modify]
                    # Reverse the attendance status
                    new_status = 'a' if current_status == 'p' else 'p'
                    employee['attendance'][date_to_modify] = new_status
                    print(f"Attendance for {date_to_modify} modified from {current_status} to {new_status}.")
                else:
                    print(f"No attendance found for {date_to_modify_str}.")
                return
        print(f"Employee with ID {emp_id} not found.")

    def get_employee_id(self, name):
        for employee in self.employee_list:
            if employee['name'].lower() == name.lower():
                return employee['Emp_id']
        return None  # If employee is not found

    def delete_employee(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                self.employee_list.remove(employee)
                print(f"Employee with ID {emp_id} deleted successfully.")
                return
        print(f"Employee with ID {emp_id} not found.")

# Main script
employee_manager = Employee()

user_active = True

while user_active:
    print("\nPlease select the operation you want to perform: ")
    print("1. Create an Employee")
    print("2. View all Employees")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Modify Attendance")  # New option for modifying attendance
    print("6. Delete Employee")
    print("7. Exit")
    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        employee_name = input("Enter employee name: ")
        employee_age = int(input("Enter employee age: "))
        employee_manager.create_employee(employee_name, employee_age)

    elif user_choice == 2:
        employee_manager.display_employee_all()

    elif user_choice == 3:
        emp_id = int(input("Enter employee ID to mark attendance: "))
        employee_manager.mark_attendance(emp_id)

    elif user_choice == 4:
        emp_id = int(input("Enter employee ID to view attendance: "))
        employee_manager.view_attendance(emp_id)

    elif user_choice == 5:  # Option to modify attendance
        emp_id = int(input("Enter employee ID to modify attendance: "))
        employee_manager.modify_attendance(emp_id)

    elif user_choice == 6:
        emp_id = int(input("Enter employee ID to delete: "))
        employee_manager.delete_employee(emp_id)

    elif user_choice == 7:
        user_active = False
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
