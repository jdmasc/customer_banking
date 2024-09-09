class Account:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest = 0

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_interest(self, interest):
        self.interest = interest

    def get_interest(self):
        return self.interest