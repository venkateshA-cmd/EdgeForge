print("=" * 60)
print("        GOOGLE EMPLOYEE ANALYTICS SYSTEM")
print("=" * 60)

# -----------------------------
# Variables and Lists
# -----------------------------
employee_names = []
employee_ages = []
employee_departments = []
employee_salaries = []

department_count = {}

valid_employees = 0
invalid_employees = 0

# -----------------------------
# Register Employees
# -----------------------------
for i in range(5):

    print(f"\nEmployee {i + 1}")

    name = input("Enter Employee Name: ")

    age = int(input("Enter Employee Age: "))

    department = input("Enter Department: ")

    salary = int(input("Enter Salary: "))

    # -----------------------------
    # Validation
    # -----------------------------
    if age <= 0 or salary <= 0 or department == "":
        print("Invalid Employee Details")
        invalid_employees += 1
        continue

    # -----------------------------
    # Store Data
    # -----------------------------
    employee_names.append(name)
    employee_ages.append(age)
    employee_departments.append(department)
    employee_salaries.append(salary)

    valid_employees += 1

    # -----------------------------
    # Dictionary Counter
    # -----------------------------
    if department in department_count:
        department_count[department] += 1
    else:
        department_count[department] = 1

# -----------------------------
# Search Employee
# -----------------------------
print("\n" + "=" * 60)

search_name = input("Enter Employee Name To Search: ")

found = False
comparisons = 0

for i in range(len(employee_names)):

    comparisons += 1

    if employee_names[i] == search_name:

        print("\nEmployee Found")

        print("Name :", employee_names[i])
        print("Age :", employee_ages[i])
        print("Department :", employee_departments[i])
        print("Salary :", employee_salaries[i])

        found = True
        break

if not found:
    print("\nEmployee Not Found")

print("Comparisons Made :", comparisons)

# -----------------------------
# Highest Salary
# -----------------------------
highest_salary = employee_salaries[0]
highest_employee = employee_names[0]

lowest_salary = employee_salaries[0]
lowest_employee = employee_names[0]

for i in range(len(employee_salaries)):

    if employee_salaries[i] > highest_salary:
        highest_salary = employee_salaries[i]
        highest_employee = employee_names[i]

    if employee_salaries[i] < lowest_salary:
        lowest_salary = employee_salaries[i]
        lowest_employee = employee_names[i]

# -----------------------------
# Highest Department
# -----------------------------
departments = list(department_count.keys())

largest_department = departments[0]
smallest_department = departments[0]

largest_count = department_count[largest_department]
smallest_count = department_count[smallest_department]

for dept in department_count:

    if department_count[dept] > largest_count:
        largest_count = department_count[dept]
        largest_department = dept

    if department_count[dept] < smallest_count:
        smallest_count = department_count[dept]
        smallest_department = dept

# -----------------------------
# Final Report
# -----------------------------
print("\n")
print("=" * 60)
print("             GOOGLE EMPLOYEE REPORT")
print("=" * 60)

print("Valid Employees   :", valid_employees)
print("Invalid Employees :", invalid_employees)

print("\nEmployee List")

for i in range(len(employee_names)):
    print("------------------------------------")
    print("Name       :", employee_names[i])
    print("Age        :", employee_ages[i])
    print("Department :", employee_departments[i])
    print("Salary     :", employee_salaries[i])

print("\nDepartment Report")

for dept in department_count:
    print(dept, ":", department_count[dept])

print("\nHighest Salary Employee")
print(highest_employee, "-", highest_salary)

print("\nLowest Salary Employee")
print(lowest_employee, "-", lowest_salary)

print("\nLargest Department")
print(largest_department, "-", largest_count)

print("\nSmallest Department")
print(smallest_department, "-", smallest_count)

print("\nSearch Comparisons :", comparisons)

print("=" * 60)
print("Report Generated Successfully")
print("=" * 60)