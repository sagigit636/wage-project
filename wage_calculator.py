import getpass


class Staff:
    def __init__(self, staff_id, days_worked):
        self._id = staff_id       # store privately
        self.days_worked = days_worked
        self.base_wage = 50        # weekly base wage in pounds
        self.daily_rate = 10       # daily rate in pounds

    def calculate_wage(self):
        return self.base_wage + (self.days_worked * self.daily_rate)

    def display_details(self):
        masked = '*' * len(self._id)  # fully masked
        print(f"ID: {masked}")
        print(f"Days Worked: {self.days_worked}")
        print(f"Total Wage: £{self.calculate_wage()}")


def main():
    # Secure input: ID hidden while typing
    user_input = getpass.getpass("Enter ID (input hidden): ")
    days = float(input("Enter number of days worked: "))

    # Create staff object
    staff_member = Staff(user_input, days)

    # Display details
    staff_member.display_details()


if __name__ == "__main__":
    main()
