# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()

class Company(object):
    def __init__(self, company_name, date_founded, employee_1, employee_2, employee_3):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employee_1 = employee_1
        self.employee_2 = employee_2
        self.employee_3 = employee_3

    def get_company_name(self):
        return self.company_name

    def get_date_founded(self):
        return self.date_founded

    def get_employees(self):
        return self.employee_1, self.employee_2, self.employee_3

walmart = Company("Wal-Mart", "1971", "Matt Kelly", "David Paul", "John Who")

print(walmart.get_company_name(),
walmart.get_date_founded(),
walmart.get_employees())

walmart.get_company_name()
walmart.get_date_founded()
walmart.get_employees()

walmart.employee_3 = "Kate Wang"
print(walmart.employee_3)




