import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(
        department,
        left_on = 'departmentId',
        right_on = "id",
        how = "left"
    )
    max_salary = merged.groupby("name_y")["salary"].transform("max")
    result = merged[merged["salary"] == max_salary]
    return result.rename(columns = {
        "name_y" : "Department",
        "name_x" : "Employee",
        "salary" : "Salary"
    })[["Department", "Employee", "Salary"]]