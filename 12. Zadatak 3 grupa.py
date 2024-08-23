class Company:
    def __init__(self, name, area, balance, max_num_of_employees):
        self._name = name
        self._area = area
        self._employees = []
        self._balance = balance
        self._max_num_of_employees = max_num_of_employees

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value

    @property
    def max_num_of_employees(self):
        return self._max_num_of_employees

    @max_num_of_employees.setter
    def max_num_of_employees(self, value):
        if value >= 0:
            self._max_num_of_employees = value

    def add_employee(self, employee):
        if len(self._employees) < self._max_num_of_employees:
            self._employees.append(employee)

    def remove_employee(self, employee_name, employee_surname):
        self._employees = [e for e in self._employees if not (e['name'] == employee_name and e['surname'] == employee_surname)]

# Testiranje klase
company = Company("Tech Innovations", "Software", 10000.0, 5)
company.add_employee({"name": "John", "surname": "Doe", "salary": 5000})
company.add_employee({"name": "Jane", "surname": "Smith", "salary": 6000})
print(company._employees)
company.remove_employee("John", "Doe")
print(company._employees)
