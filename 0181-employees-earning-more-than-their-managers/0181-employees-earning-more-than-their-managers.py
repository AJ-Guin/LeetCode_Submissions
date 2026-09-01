import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merge = employee.merge(
        employee,
        left_on = 'managerId',
        right_on = 'id',
    )

    result = merge[merge["salary_x"]> merge['salary_y']]
    return result[["name_x"]].rename(columns = {'name_x' : 'Employee'})