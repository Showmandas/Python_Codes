#Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

init_dict=dict.fromkeys(employees,defaults)
print(init_dict)