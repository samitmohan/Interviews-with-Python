import datetime


class Employee:
    # class variable
    raise_amount = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + last + "@company.com"

    # allows us to use it as an attribute not a function/method
    @property
    def email(self) -> str:
        return f"{self.first}.{self.last}@email.com"

    @property
    def full_name(self) -> str:
        return self.first + " " + self.last

    @full_name.setter  # This decorator associates this method as the setter for 'full_name'
    def full_name(self, name: str):
        parts = name.split(" ")
        if parts:
            self.first = parts[0]
            self.last = parts[1]

    # self = instance of the class here which gets automatically passed
    def apply_raise(self) -> int:
        self.pay *= self.raise_amount
        return self.pay

    # for class methods we need to use a decorator (we pass class, amount)
    @classmethod
    def apply_raise_class(cls, amount):
        """
        working with class not instance here
        """
        cls.raise_amount = amount

    # class methods as alternative constructors -> what does this mean
    @classmethod
    def from_String(cls, parsed_str) -> str:
        """
        passes a specific string format and parses it into first name last name email
        """
        first, last, pay = parsed_str.split("-")
        return cls(first, last, pay)  # creates new employee

    # static methods = regular functions but included in class bcs they have some logical connection it it
    @staticmethod
    def is_workDay(day) -> bool:
        """
        not using class or self anywhere here = staticmethod
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # Dunder Methods
    def __repr__(self) -> str:
        """
        for coders, returns whatever you've passed in employee
        """
        return f"Employee('{self.first}', '{self.last}')"

    def __str__(self) -> str:
        """
        uses repr as a backup
        for users
        """
        return f"{self.full_name} - {self.email}"

    # dunder method for + for classes
    def __add__(self, other) -> int:
        self.pay + other.pay

    # len method for classes
    def __len__(self) -> int:
        return len(self.full_name)


emp1 = Employee("samit", "mohan", 4000)
# print(emp1.raise_amount)
# emp1.apply_raise_class(2) # class method from the instance (still changes) but not widely used
Employee.apply_raise_class(2)  # this is used
# print(emp1.raise_amount)
parsed_emp1 = "Mihica-Mohan-7000"

# should return first name last name pay (alt constructor)
new_emp = Employee.from_String(parsed_emp1)
# print(new_emp.full_name())

# static method test
my_date = datetime.date(2025, 5, 23)
# print(new_emp.is_workDay(my_date))


# print(emp1.__dict__)
# print(emp1.apply_raise())
# print(Employee.__dict__) here we are passsing class (this is how emp1 works internally)


# Developer and Manager subclass inheriting
class Developer(Employee):
    def __init__(self, first, last, pay, lang) -> None:
        super().__init__(first, last, pay)  # inherits specific from super class
        self.lang = lang


class Manager(Employee):
    """
    You never want to pass mutable data types as default arguments in parameters
    Inherits all from super class by default if you don't put anything here (no custom param for Dev class)
    """

    def __init__(self, first, last, pay, employees=None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        print([e.full_name for e in self.employees])


dev0 = Developer("tom", "croose", 100000, "python")
dev1 = Developer("tom", "cruise", 200000, "java")
# print(dev1.email)
# print(dev1.lang)
# print(help(dev0)) # shows all info
# isinstance() and issubclass() works to check

manager0 = Manager("sam", "altman", 500000, [dev0])
# print(manager0.email)
manager0.add_emp(dev1)
manager0.print_emp()
print(emp1)  # should print __repr__ and __str__ instead of generator object
print(len(emp1))  # should print 11 (samitmohan)

# Decorators -> getter setter deleter

emp_dec = Employee("Jim", "Halpert", "4000")
# print(emp_dec.first)
# print(emp_dec.full_name())
# print(emp_dec.email)
# print("---")
# emp_dec.first = "James"
print(emp_dec.first)
# print(emp_dec.full_name())
# print(emp_dec.email) # this still jimhapert@company.com -> how to treat this as an attribute
# we want wherever james changed, it should be reflected -> use getters / setters or decorators in python {create email method}
# now we can do email(), but what if we dont want () -> cuz we'll need to change it -> so how to access it like an attribute -> decorator
# print(emp_dec.email())
# print(emp_dec.email)
emp_dec.full_name = "Tom Cruise"
print(emp_dec.full_name)
