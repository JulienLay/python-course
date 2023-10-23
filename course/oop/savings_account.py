from bank_account import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, name:str, balance:float, interest_rate:float=0.003) -> None:
        BankAccount.__init__(self, name, balance)
        self.interest_rate = interest_rate

    def set_rate(self, value:float) -> None:
        self.interest_rate = value
        print(f'Changing interest rate to {value}.')

    def capitalization(self, month_account:int) -> None:
        for i in range(1, month_account+1):
            self.balance += self.balance*self.interest_rate
        print(f'Your capitalization is {round((self.balance), 2)} dollars for {month_account} months.')

print("--------------")
juju_account = SavingAccount('Julien', 1000)
print(juju_account)
juju_account.set_rate(0.003)
juju_account.capitalization(12)