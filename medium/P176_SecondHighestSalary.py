import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if (employee.shape[0] <= 1):
       second = {
        "SecondHighestSalary": [None] 
    }                                                                       # if there's 0 or 1 employee, there's no second highest-salary possible
    
    else:    
        employee = employee.sort_values(by='salary', ascending=False)       

        i = 0
        while (i < employee.shape[0] and employee.iloc[i]["salary"] == employee.iloc[0]["salary"]):
            i += 1    
        
        if (i == employee.shape[0]):
               second = {
                        "SecondHighestSalary": [None] 
                }
                 
        else:
                second = {
                        "SecondHighestSalary": [employee.iloc[i]["salary"]] 
                }

    return pd.DataFrame(second)
