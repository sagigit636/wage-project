import getpass

class Staff:
    def __init__(self, staff_id, days_worked):
        self._staff_id = staff_id  # store privately
        self.days_worked = days_worked
        self.base_wage = 50        # weekly base wage in pounds
        self.daily_rate = 10       # daily rate in pounds

    def calculate_wage(self):
        return self.base_wage + (self.days_worked * self.daily_rate)

    def get_masked_id(self):
        # Fully mask staff ID: same length of asterisks
        return '*' * len(self._staff_id)

    def display_details(self):
        print(f"Staff ID: {self.get_masked_id()}")
        print(f"Days Worked: {self.days_worked}")
        print(f"Total Wage: £{self.calculate_wage()}")


def test_func():
    # Secure input: Staff ID hidden while typing
    staff_id = getpass.getpass("Enter Staff ID (input hidden): ")
    days = float(input("Enter number of days worked: "))

    # Create object
    staff_member = Staff(staff_id, days)

    # Display results
    staff_member.display_details()


test_func()
