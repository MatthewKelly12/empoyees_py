class Company():
    def __init__(self, company_name, date_founded, employees):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = employees

    def get_company_name(self):
        return self.company_name

    def get_date_founded(self):
        return self.date_founded

    def get_employees(self):
      for x in self.employees:
         print(x.first_name, x.last_name, x.hire_date)

class Employee():
    def __init__(self, first_name, last_name, hire_date):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
# make function to put employees in appropriate company
# def company_employees ():

matt = Employee("Matt", "Kelly", "July 1, 2018")
greg = Employee("Greg", "Smelly", "July 2, 2018")
walmart_employees = list()
walmart_employees.append(matt)
walmart_employees.append(greg)

walmart = Company("Wal-Mart", "1971", walmart_employees)

# print(walmart.get_company_name(),
# walmart.get_date_founded())

for x in walmart_employees:
  print(x.first_name, x.last_name, x.hire_date)

walmart.get_employees()






