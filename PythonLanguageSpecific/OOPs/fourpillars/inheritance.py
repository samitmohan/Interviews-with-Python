"""
Types of Inheritance:
    Single Inheritance: One parent class
    Multiple Inheritance: Multiple parent classes
    Multilevel Inheritance: Chain of inheritance
    Hierarchical Inheritance: Multiple children from one parent
"""

from datetime import datetime


class Employee:
    # class variables
    company_name = "OpenAI"
    total_employees = 0

    def __init__(self, name, emp_id, salary, **kwargs) -> None:
        super().__init__(**kwargs)  # Call super() to continue the MRO chain
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.hire_date = datetime.now()
        # update class variable
        Employee.total_employees += 1

    def get_info(self):
        return f"Employee : {self.name} ID : {self.emp_id}"

    def calculate_annual_salary(self):
        return self.salary * 12

    def get_benefits(self) -> list:
        """Basic benefits for all employees."""
        return ["Health Insurance", "Paid Time Off"]

    @classmethod
    def get_company_info(cls):
        return f"Company : {cls.company_name}, Total Employees : {cls.total_employees}"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.name}"


# Single Inheritance
class Dev(Employee):
    def __init__(self, name, emp_id, salary, prog_languages, experience, **kwargs):
        super().__init__(name=name, emp_id=emp_id, salary=salary, **kwargs)
        self.prog_languages = prog_languages
        self.experience = experience
        self.projects_completed = 0

    # method overriding
    def get_info(self) -> str:
        """Override parent get_info"""
        base_info = super().get_info()
        return f"{base_info}, Languages : {self.prog_languages}, Projects : {self.projects_completed}"

    # new method specific to dev
    def add_programming_language(self, language: str) -> None:
        """Add a new programming language to the developer's skillset."""
        if language not in self.prog_languages:
            self.prog_languages.append(language)
            print(f"Added {language} to {self.name}'s skillset")

    def complete_project(self) -> None:
        """Mark a project as completed."""
        self.projects_completed += 1
        print(f"{self.name} completed project #{self.projects_completed}")

    # Override benefits method
    def get_benefits(self) -> list:
        """Enhanced benefits for developers."""
        base_benefits = super().get_benefits()  # Get parent benefits
        developer_benefits = ["Learning Stipend", "Flexible Hours", "Remote Work"]
        return base_benefits + developer_benefits

    # Calculate bonus based on experience and projects
    def calculate_bonus(self) -> float:
        """Calculate performance bonus."""
        base_bonus = self.salary * 0.1  # 10% base bonus
        experience_bonus = self.experience * 500
        project_bonus = self.projects_completed * 1000
        return base_bonus + experience_bonus + project_bonus


# Manager Inheritance


class Manager(Employee):
    """Manager class inheriting from Employee."""

    def __init__(self, name: str, employee_id: str, salary: float, department: str):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.team_members = []

    def add_team_member(self, employee: Employee) -> None:
        """Add an employee to the manager's team."""
        self.team_members.append(employee)
        print(f"Added {employee.name} to {self.name}'s team")

    def get_team_info(self) -> str:
        """Get information about the team."""
        if not self.team_members:
            return f"{self.name} manages no direct reports"

        team_names = [member.name for member in self.team_members]
        return f"{self.name} manages: {', '.join(team_names)}"

    # override
    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Department: {self.department}"

    def get_benefits(self) -> list:
        base_benefits = super().get_benefits()
        manager_benefits = [
            "Management Training",
            "Executive Parking",
            "Expense Account",
        ]
        return base_benefits + manager_benefits


# Multiple Inheritance -> From Dev and Consultant <- TechnicalConsultant
class Consultant:
    def __init__(self, hourly_rate: float, **kwargs) -> None:
        super().__init__(**kwargs)  # important for multiple inheritance
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def log_hrs(self, hours: float) -> None:
        self.hours_worked += hours
        print(f"Logged {hours} hours. Total: {self.hours_worked}")

    def calculate_consultant_pay(self) -> float:
        """Calculate pay based on hourly rate."""
        return self.hourly_rate * self.hours_worked


class TechnicalConsultant(Dev, Consultant):
    def __init__(
        self,
        name: str,
        emp_id: str,
        salary: float,
        prog_languages: list,
        experience: int,
        hourly_rate: float,
        client_name: str,
    ):
        super().__init__(
            name=name,
            emp_id=emp_id,
            salary=salary,
            prog_languages=prog_languages,
            experience=experience,
            hourly_rate=hourly_rate,
        )
        self.client_name = client_name

    def get_info(self) -> str:
        """Override to include consultant info."""
        dev_info = Dev.get_info(self)  # Explicitly call Developer's method
        return f"{dev_info}, Client: {self.client_name}, Rate: ${self.hourly_rate}/hr"

    def get_benefits(self) -> list:
        """Combine benefits from both parent classes."""
        return list(set(Dev.get_benefits(self)))  # Remove duplicates


if __name__ == "__main__":
    print("=== Inheritance Demonstration ===\n")

    emp = Employee("Alice Johnson", "EMP001", 5000)
    print(f"Base Employee: {emp.get_info()}")
    print(f"Benefits: {emp.get_benefits()}")
    print(f"Annual Salary: ${emp.calculate_annual_salary():,.2f}")

    print("\n" + "-" * 50 + "\n")

    dev = Dev("Bob Smith", "DEV001", 7000, ["Python", "JavaScript"], 5)
    print(f"Developer: {dev.get_info()}")  # Overridden method
    print(f"Benefits: {dev.get_benefits()}")  # Enhanced benefits
    print(f"Annual Salary: ${dev.calculate_annual_salary():,.2f}")

    # Use developer-specific methods
    dev.add_programming_language("Go")
    dev.complete_project()
    dev.complete_project()
    print(f"Bonus: ${dev.calculate_bonus():,.2f}")

    print("\n" + "-" * 50 + "\n")

    mgr = Manager("Carol Davis", "MGR001", 9000, "Engineering")
    mgr.add_team_member(dev)
    mgr.add_team_member(emp)
    print(f"Manager: {mgr.get_info()}")
    print(f"Team: {mgr.get_team_info()}")
    print(f"Benefits: {mgr.get_benefits()}")

    print("\n" + "-" * 50 + "\n")

    # Create technical consultant (multiple inheritance)
    consultant = TechnicalConsultant(
        name="David Wilson",
        emp_id="CON001",
        salary=6000,
        prog_languages=["Python", "Java", "C++"],
        experience=8,
        hourly_rate=150,
        client_name="ABC Corp",
    )

    print(f"Technical Consultant: {consultant.get_info()}")
    consultant.log_hrs(40)
    consultant.complete_project()
    print(f"Consultant Pay: ${consultant.calculate_consultant_pay():,.2f}")
    print(f"Bonus: ${consultant.calculate_bonus():,.2f}")

    print("\n" + "-" * 50 + "\n")

    # Demonstrate Method Resolution Order (MRO)
    print("Method Resolution Order for TechnicalConsultant:")
    for i, cls in enumerate(TechnicalConsultant.__mro__):
        print(f"  {i + 1}. {cls.__name__}")

    print(f"\n{Employee.get_company_info()}")
