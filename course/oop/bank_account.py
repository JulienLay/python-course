class BankAccount:
    def __init__(self, name:str='John', balance:float=1000) -> None:
        self.name = name
        self.balance = balance

    def deposit(self, amount:float) -> None:
        self.balance += amount
        print(f'You deposit {amount} dollar(s). Your actual deposit is {self.balance}.')

    def withdraw(self, amount:float) -> None:
        if (self.balance-amount >= 0):
            self.balance -= amount
            print(f'You withdraw {amount} dollar(s). Your actual deposit is {self.balance}.')

        else:
            print(f'Your actual deposit is {self.balance}. You can\'t withdraw this much money. Withdraw failed.')

    def display(self) -> None:
        print(f'The deposit of {self.name} is {self.balance} dollars.')

    def __str__(self) -> str:
        return f'{self.name} - {self.balance}'

account = BankAccount('Julien', 3000000)
account.withdraw(20000.25)
account.deposit(200.66)
account.display()
# le __str__ s'affiche si on affiche l'instance de la classe avec le print suivant
print(account)