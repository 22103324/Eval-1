employee_directory = {}

def add_employee(emp_id, name, dep, salary):
    if emp_id in employee_directory:
        print(f"Employee id {emp_id} already exists.")
    else:
        employee_directory[emp_id] = {
            'Name': name,
            'Dep': dep,
            'Salary': salary
        }
        print(f"Employee {name} added.")

def update_employee(emp_id, name=None, dep=None, salary=None):
    if emp_id not in employee_directory:
        print(f"Employee id {emp_id} not found.")
    else:
        if name:
            employee_directory[emp_id]['Name'] = name
        if dep:
            employee_directory[emp_id]['Dep'] = dep
        if salary:
            employee_directory[emp_id]['Salary'] = salary
        print(f"Employee id {emp_id} updated.")

def search_employee(emp_id):
    if emp_id in employee_directory:
        employee = employee_directory[emp_id]
        print(f"Employee id: {emp_id}")
        print(f"Name: {employee['Name']}")
        print(f"Department: {employee['Dep']}")
        print(f"Salary: {employee['Salary']}")
    else:
        print(f"Employee id {emp_id} not found.")

def department_report():
    department_summary = {}
    for emp_id, details in employee_directory.items():
        department = details['Dep']
        if department not in department_summary:
            department_summary[department] = []
        department_summary[department].append(details['Name'])
    
    for department, employees in department_summary.items():
        print(f"Department: {department}")
        print("Employees: " + ", ".join(employees))

if __name__ == "__main__":
    add_employee(1, 'Alice', 'Eng', 70000)
    add_employee(2, 'Bob', 'Mark', 60000)
    add_employee(3, 'Charlie', 'Eng', 75000)

    print("Search employee with id 1:")
    search_employee(1)

    print("Update salary of employee with id 2:")
    update_employee(2, salary=65000)

    print("Search employee with id 2:")
    search_employee(2)

    print("Department-wise employee report:")
    department_report()
