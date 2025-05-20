class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0 #Encapsulation
    
    def check_balance(self):
        return self._balance
    
    def deposite(self, amount):
        self._balance += amount
        print(f"Updeted Balance: {self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Available Balance: {self._balance}")
        else:
            print("Insufficient Balance!!")

class SavingsAccount(Account):
    def calculate_interest(self):
        INTEREST_RATE = 0.4 #%4
        interest = self._balance * INTEREST_RATE
        print(f"Interest Rate for your balance is {interest}")

class CurrentAccount(Account):
    
    def withdraw(self, amount):
        OVERDRAT_LIMIT = 2000
        if (self._balance + OVERDRAT_LIMIT) >= amount:
            self._balance -= amount
            print(f"Available Balance: {self._balance}")
        else:
            print("Insufficient Balance!!")

class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__accounts = {}
        
    def create_account(self, id, holder_name, type):
        if type == "savings":
            new_account = SavingsAccount(id, holder_name)
            print("Your Savings Account has been created succufully")
        elif type == "current":
            new_account = CurrentAccount(id, holder_name)
            print("Your Current Account has been create successfully")
        self.__accounts[id] = new_account
        return new_account
    
hbk = Bank("Harsith Bank of Karnataka", "Tumkur")

harshith_savings_account = hbk.create_account(1,"Harshith Gowda H L", "savings")

harshith_current_account = hbk.create_account(2,"Harshith Gowda H L", "current")

def menu():
    print("-- Banking System --")
    print("1.Check Balance\n2. Withdraw\n3. Deposite")

while True:
    account_type_input = input("Enter Account Type (savings, current): ")

    if account_type_input == "savings":
        menu()
        print("4. Calculate Interest Rate\n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice in [1,2,3,4]:
            match choice :
                case 1: 
                    print(f"Available Balance {harshith_savings_account.check_balance()}")
                case 2:
                    withdraw_amount = int(input("Enter Withdraw amount: "))
                    harshith_savings_account.withdraw(amount=withdraw_amount)
                case 3:
                    deposite_amount = int(input("Enter Deposite Amount: "))
                    harshith_savings_account.deposite(deposite_amount)
                case 4:
                    harshith_savings_account.calculate_interest()
        elif choice == 5:
            print("Quiting...")
            break
        else:
            print("Invalid choice. Try Again!")

    elif account_type_input == "current":
        menu()
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice in [1,2,3]:
            match choice:
                case 1: 
                    print(f"Available Balance {harshith_current_account.check_balance()}")
                case 2:
                    withdraw_amount = int(input("Enter Withdraw amount: "))
                    harshith_current_account.withdraw(amount=withdraw_amount)
                case 3:
                    deposite_amount = int(input("Enter Deposite Amount: "))
                    harshith_current_account.deposite(deposite_amount)
        elif choice == 4:
            print("Quiting...")
            break
        else:
            print("Invalid choice. Try Again!")

    else:
        print("Invalid Account Type. Try Again!")