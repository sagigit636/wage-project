class Staff:
    def __init__(self, staff_id, days_worked):
#        self.staff_id = staff_id
        self.days_worked = days_worked
        self.base_wage = 50        # weekly base wage in pounds
        self.daily_rate = 10      # hourly rate in pounds

    def calculate_wage(self):
        total_wage = self.base_wage + (self.days_worked * self.daily_rate)
        return total_wage

    def display_details(self):
#        print(f"Staff ID: {self.staff_id}")
        print(f"Hours Worked: {self.days_worked}")
        print(f"Total Wage: £{self.calculate_wage()}")


def test_func():
    # Taking user input
#    staff_id = input("Enter Staff ID: ")
    hours = float(input("Enter number of days worked: "))

    # Create object
#    staff_member = Staff(staff_id, hours)

    # Display results
    staff_member.display_details()


test_func()
