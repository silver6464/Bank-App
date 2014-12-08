﻿from lettuce import *
from bank.account import Account
from bank.bank import Bank
@step(u'account number 0001 is a valid account')
def given_account_number_0001_is_a_valid_account(step):
	account = Account(0001, 50)
	bank = Bank()
	bank.add_account(account)