# Task 1.1

import pandas as pd

data = {
   'Name': ['Alice', 'Bob', 'Charlie'],
   'Age': [25, 30, 35],
   'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print (task1_data_frame)

#Task 1.2

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

#Task 1.3

task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older["Age"] + 1
print (task1_older)

#Task 1.4

task1_older.to_csv('employees.csv', index = False)


#Task 2.1
 
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

#Task 2.2

json_employees = pd.read_json("additional_employees.json")
print (json_employees)

#Task 2.3

more_employees = pd.concat([task2_employees,json_employees],ignore_index=True)
print(more_employees)

#Task 3.1

first_three = more_employees.head(3)
print (first_three)

#Task 3.2

last_two = more_employees.tail(2)
print(last_two)

#Task 3.3

employee_shape = more_employees.shape
print(employee_shape)

#Task 3.4

print(more_employees.info())

#Task 4.1

dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)
clean_data = dirty_data.copy()

#Task 4.2

clean_data = clean_data.drop_duplicates()
print(clean_data)

#Task 4.3

clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors='coerce')
print(clean_data)

#Task 4.4

clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'] , errors= 'coerce')
print(clean_data)

#Task 4.5

clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print(clean_data)

#Task 4.6

clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'],errors='coerce')
print(clean_data)

#Task 4.7

clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Name'] = clean_data['Name'].str.upper()

clean_data['Department'] = clean_data['Department'].str.strip()
clean_data['Department'] = clean_data ['Department'].str.upper()

print(clean_data)