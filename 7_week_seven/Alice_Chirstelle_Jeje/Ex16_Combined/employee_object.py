from employee import Employee

anna = Employee('Anna', 'Dimitri')
anna_job_title = anna.set_job_title('Staff writer')
anna_starting_salary = anna.set_base_salary(30000)
anna_original_fte = anna.set_fte(1.0)
print(anna)

# Alice updated this to test the apply_raise function:
anna_first_raise = anna.apply_raise(.04)
print("Salary after first raise: ", anna_first_raise)
print("New base salary: ", anna.get_base_salary())

anna_second_raise = anna.apply_raise(0.02)
print("Salary after second raise: ", anna_second_raise)
print("New base salary: ", anna.get_base_salary())

print("Actual salary at", anna.get_fte(), "FTE is: ", anna.calculate_actual_salary())

anna_new_fte = anna.set_fte(0.8)
print("New FTE is: ", anna.get_fte())
print("New, actual salary at ", anna.get_fte(), "FTE is: ", anna.calculate_actual_salary())
# If we print the variable it returns 'None'?
print(anna_new_fte)
print(anna)