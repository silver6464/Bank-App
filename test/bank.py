class Bank(object):
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account.balance
    def get_account_balance(self, account_number):
        return self.accounts.get(account_number)
    def account_withdraw(self, account_number,amount):    	
    	self.accounts[account_number] -= amount
    def does_account_exist(self,account_number):
    	return self.accounts[account_number]
    	
