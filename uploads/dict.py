dept_dict = {
    "AI":3,
    "HR":2,
    "Finance":1
}

print(f"AI has {dept_dict['AI']} employees.")
print(f"HR has {dept_dict['HR']} employees.")
print(f"Finance has {dept_dict['Finance']} employees.")

dept_dict = {
    "AI": 3,
    "HR": 2,
    "Finance": 1,
    "Cyber": 4
}

# Get the first department to initialize
departments = list(dept_dict.keys())

highest_department = departments[0]
lowest_department = departments[0]

highest_count = dept_dict[highest_department]
lowest_count = dept_dict[lowest_department]

# Traverse the dictionary
for department in dept_dict:
    count = dept_dict[department]

    # Find highest
    if count > highest_count:
        highest_count = count
        highest_department = department

    # Find lowest
    if count < lowest_count:
        lowest_count = count
        lowest_department = department

print("========== REPORT ==========")
print(f"Highest Department : {highest_department}")
print(f"Employee Count     : {highest_count}")

print()

print(f"Lowest Department  : {lowest_department}")
print(f"Employee Count     : {lowest_count}")


    

    