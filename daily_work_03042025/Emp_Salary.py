# Problem : Employee Salary Adjustment System using lambdas

employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]

update_salary = lambda emp: { **emp,  
    "salary": emp["salary"] + (emp["salary"] * 0.1) if emp["rating"] in [4, 5] 
                               else emp["salary"] + (emp["salary"] * 0.05) if emp["rating"] == 3 
                               else emp["salary"] - (emp["salary"] * 0.03)  
}
updated_employees = list(map(update_salary, employees))
print(updated_employees)
