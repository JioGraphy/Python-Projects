
# Parent Class - Super Class
class Employee:

    def __init__(self, fname, lname):
        # setting class properties from the passed-in values
        self.fname = fname
        self.lname = lname
    

# Employee ---> SalaryEmployee
class SalaryEmployee(Employee):

    def __init__(self, fname, lname, salary): # Take note of the parameters position
        # calls the init method of the parent class, to just re-use the properties.
        super().__init__(fname, lname) 
        self.salary = salary
    
    def calculate_paycheck(self):
        salary = self.salary / 52
        return salary


# Employee ---> HourlyEmployee
class HourlyEmployee(Employee):
    
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
    
    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate



# Multiple Levels of Inheritance
# SalaryEmployee ---> CommisionEmployee
class CommissionEmployee(SalaryEmployee):

    def __init__(self, fname, lname, salary, sales_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate

    def calculate_paycheck(self):
        regular_salary =  super().calculate_paycheck()
        total_commission = self.sales_num * self.com_rate
        return regular_salary + total_commission