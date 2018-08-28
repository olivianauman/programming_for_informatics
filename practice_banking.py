'''
This program is designed to mimic the DCCU Banking system! Do what you will. 
'''
class Bank(object):
    registry = []
    
    def __init__(self, name, checking_balance, savings_balance):
        self.account_holder = name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        if name not in registry:
            registry[name]: (savings_balance, checking_balance)
            
    
     
     
    
