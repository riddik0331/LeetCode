import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(
        employee,
        how='left',
        left_on='managerId',
        right_on='id',
        suffixes=('', '_mgr')
    )
    res = merged_df[merged_df['salary'] > merged_df['salary_mgr']]
    
    return res[['name']].rename(columns={'name': 'Employee'})[['Employee']]
