# from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee


# class Company:

#     def __init__(self):
#         self.employees = []

#     def add_employees(self, new_employee):
#         self.employees.append(new_employee)

#     def display_employee(self):
#         print('Current Employee: ')
#         for i in self.employees:
#             print(i.fname, i.lname)
#         print('---------------------')

#     def pay_employees(self):
#         print('Paying Employees:')
#         for i in self.employees:
#             print('Paycheck for', i.fname, i.lname)
#             # print('Amount {}'.format(i.calculate_paycheck()))
#             print(f'Amount: ${i.calculate_paycheck():,.2f}')
#             print('--------------------')


# # Main Program
# def main():

#     my_company = Company()
#     employee_1 = SalaryEmployee('George', 'Estellore', 15000)

#     my_company = Company()
#     employee_2 = HourlyEmployee('Georgina', 'Willson', 25, 50)

#     my_company = Company()
#     employee_3 = CommissionEmployee('Bob', 'Brown', 3000, 5, 200)

#     my_company.add_employees(employee_1)
#     my_company.add_employees(employee_2)
#     my_company.add_employees(employee_3)

#     # print(my_company.employees)
#     my_company.display_employee()
#     my_company.pay_employees()

# # Invoking main function
# main()

# # import sys
# # print(sys.path)
