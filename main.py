class Atm:

    def __init__(self):
        self.pin = ""
        self.amount = 0
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input("""
            Hello, How would you like to proceed?
            1. Enter 1 to Create pin.
            2. Enter 2 to Deposit amount.
            3. Enter 3 to Withdraw money.
            4. Enter 4 to Check balance.
            5. Enter 5 to Exit.
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Exit")

    def create_pin(self):
        self.pin = input("Enter your Pin: ")
        print("Pin set Successfully")

    def deposit(self):
        temporary = input("Enter your Pin: ")
        if temporary == self.pin:
            amount = int(input("Enter your Deposit Amount: "))
            self.balance = self.balance + amount
            print("Deposit Successful")
        else:
            print("Invalid pin.")

    def withdraw(self):
        temporary = input("Enter your Pin: ")
        if temporary == self.pin:
            amount = int(input("Enter your Withdrawal Amount: "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Operation Successful")
            else:
                print("Amount is Invalid or Insufficient Fund.")
        else:
            print("Invalid Pin.")

    def check_balance(self):
        temporary = input("Enter your Pin: ")
        if temporary == self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")


proceed_atm = Atm()
proceed_atm.deposit()
proceed_atm.withdraw()
proceed_atm.check_balance()
