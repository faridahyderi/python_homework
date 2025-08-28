
#Task 2
import csv
import traceback
import os

def read_employees ():
    data = {} #dictionary
    rows = [] #List

    try:
        with open('../csv/employees.csv','r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row
                else:
                    rows.append(row)    
            data["rows"] = rows
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [f'File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}' for trace in trace_back]
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return data

employees = read_employees()
print(employees)           

#Task 3

def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Column '{column_name}' not found.")

employee_id_column = column_index("employee_id")
print(f"Employee ID Column Index: {employee_id_column}")

#Task 4

def first_name(row_number):
        try: 
            first_name_column = column_index("first_name")
            return employees["rows"][row_number][first_name_column]
        except IndexError:
            print(f"Row {row_number} not found.")

name = first_name(5)
print(f"First Name at Row 5: {name}")

#Task 5

def employee_find(employee_id):
    def employee_match(row):
       return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches    

employee_id = 15
matches = employee_find(employee_id)
print(f"Employees found with ID {employee_id}: {matches}")

#Task 6

def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#Task 7

def sort_by_last_name():
    try:
        last_name_column = column_index("last_name")
        employees["rows"].sort(key =lambda row: row[last_name_column])
        return employees["rows"]
    except Exception as e:
        print(f"An error occurred: {e}")

sorted_rows = sort_by_last_name()
print("\nSorted Employees by Last Name:")
for row in sorted_rows:
    print(row)      

#Task 8

def employee_dict(row):
    try:
        employee = {key: value for key, value in zip(employees["fields"],row) if key !="employee_id"} 
        return employee
    except Exception as e:
        print(f"An error occurred: {e}")

sample_row = employees["rows"][0]
result = employee_dict(sample_row)
print("\nEmployee Dict:")
print(result)

#Task 9

def all_employees_dict():
    try:
        all_employee = {}
        for row in employees["rows"]:
         employee_id = str(row[column_index("employee_id")])
         all_employee[employee_id] = employee_dict(row)
        return all_employee
    except Exception as e:
         print(f"An error occurred: {e}")

result = all_employees_dict()
print("\nAll Employees Dict:")
print(result)

#Task 10

def get_this_value():
    return os.getenv("THISVALUE")

result = get_this_value
print(f"Value of THISVALUE: {result}")

#Task 11
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Farida")
print(custom_module.secret)


#Task 12
import csv

def read_minutes():
    # Helper function to read a CSV file and convert rows to tuples
    def read_csv(file_path):
        try:
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                fields = next(reader)  # The first row is the header (fields)
                rows = [tuple(row) for row in reader]  # Converting each row to a tuple
                return {"fields": fields, "rows": rows}
        except Exception as e:
            print(f"Error reading : {e}")
            
    
    # Reading both CSV files using the helper function
    minutes1 = read_csv("../csv/minutes1.csv")
    minutes2 = read_csv("../csv/minutes2.csv")
    
    # Return both dictionaries
    return minutes1, minutes2


# Call the function and store the results in global variables
minutes1, minutes2 = read_minutes()

print("Minutes1 Dictionary:", minutes1)
print("Minutes2 Dictionary:", minutes2)


#Task 13

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    combined_set = set1.union(set2)
    return combined_set

minutes_set = create_minutes_set()
print("\nCombined Minutes Set:")
print(minutes_set)

#Task 14

from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)

    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list

minutes_list = create_minutes_list()

print("\nMinutes List:")
for item in minutes_list:
    print(item)

#Task 15

import csv

def write_sorted_list():
    # Step 1: Sort minutes_list by the datetime object
    minutes_list.sort(key = lambda x: x[1]) 

    # Step 2: Convert datetime back to string using map
    converted_minutes_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

    # Step 3: Write the data to a CSV file
    with open('./minutes.csv','w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_minutes_list)

    return converted_minutes_list    

result = write_sorted_list()
print("\nSorted Minutes List:")
print(result)