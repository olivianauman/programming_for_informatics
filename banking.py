#Olivia Nauman
#Homework 9


#make parent class called Bank which contains attributes for the subclasses checking and savings to inherit
class Bank(object):
    
      #attributes of the class  
    def __init__(self, name, balance):
        self.AccountBalance = balance
        self.AccountHolder = name
        
      #get acct balance         
    def getAccountBalance(self):
            return self.AccountBalance
      #set acct balance  
    def setAccountBalance(self, balance):
        self.AccountBalance = balance  
        
#get account holder
    def getAccountHolder(self):
        return self.AccountHolder
    #set account holder
    def setAccountHolder(self, AccountHolder):
        self.AccountHolder = AccountHolder 
        
       #add money to an acct 
    def credit(self,value):
        self.credit = self.AccountBalance + value
        
       #remove money from an acct. Let the user know if there isn't enough $$ 
    def debit(self,value):
        if value > self.AccountBalance:
            return "The account does not contain enough money for this transaction."
        elif value <= self.AccountBalance:
            self.debit = self.AccountBalance + value    
        
# create subclass checking w attributes of class and balance 
class Checking(Bank):
    
    def __init__(self, name, balance):
        self.AccountBalance = balance
        
        
    def getAccountBalance(self):
        return self.AccountBalance
    
    def setAccountBalance(self, balance):
        self.AccountBalance = balance
        
#create a subclass savings  w attributes of class and balance
class Savings(Bank):
    def __init__(self, name, balance):
            self.AccountBalance = balance
            
    def getAccountBalance(self):
            return self.AccountBalance
        
    def setAccountBalance(self, balance):
        self.AccountBalance = balance  

#read the file in of names acct type and initial account balances, split it into lines. 
def readFile(filename):
    #the try/except will assume proper input is used, and will otherwise give an error notice
    try:
        with open(filename, 'r') as f:
            data = f.read().splitlines()
        #make a list of smaller lists, each being an entry of name, account type, and account balance by splitting these entried by the comma.
        account_list = []
        for line in data:
            account_list.append(line.split(','))
        return account_list
    except NameError or TypeError:
        print ( "Incorrect Input!" )
        
#read the file in of names, acct type, debit/credit, amount
def readActionFile(filename):
    #the try/except will assume proper input is used, and will otherwise give an error notice
    try: 
        #open the file and split it into lines splitting that list into smaller lists at the comma
        with open(filename, 'r') as f:
            data = f.read().splitlines()
        account_actions_list = []
        for line in data:
            account_actions_list.append(line.split(','))
        #return an updated list that is the file given translated into a usable format
        return account_actions_list  
    except NameError or TypeError:
        print ( "Incorrect Input!" )
#this function creates the savings and checking accts
def create_Checking_and_Savings(account_list):
    #two empty dictionaries that will become all of bank accts
    checking_dict = {}
    savings_dict = {}
    #for each mini list in the list of files
    for element in account_list:
        name = element[0]
        account_type = element[1]
        balance = element[2]
        #if the account type says checking call on the chcking subclass
        if account_type == "Checking":
            x = Checking(name,balance)
            checking_dict[name] = Bank(x.AccountBalance)
        #if the account type says savings call on yhe savings subclass
        elif account_type == "Savings":
            y = Savings(name,balance)
            savings_dict[name] = Bank(y.AccountBalance)
        #if they want something other checkings and or savings raise an error
        else:
            print ("Account type not recognized!")  
    #return the two dictionary files
    return checking_dict, savings_dict

#adjust acct balances based on the second file
def transactions(account_actions_list, savings_dict, checking_dict):
    #for each mini list in the actions list
    for element in account_actions_list:
        try:
        #seperate the values into variables
            name = element[0]
            transaction_type = element[1]
            account_type = element[2]
            amount = element[3]  
            #find the element in the dictionaries
            person_savings = savings_dict[name]
            person_checking = checking_dict[name]
            #if its a checking account, add or remove money as specified
            if account_type == "Checking" and name in checking_dict:
                if transaction_type == "Credit":
                    person_checking.credit(amount)
                    print(name + transaction_type + account_type + str(person_checking.AccountBalance))
                elif transaction_type == "Debit" and person_checking.AccountBalance >= amount:
                    person_checking.debit(amount)   
                    print(name + transaction_type + account_type + str(person_checking.AccountBalance))
            #if its a savings acct add or remove money as specified
            elif account_type == "Savings" and name in savings_dict:
                if transaction_type == "Credit":
                    person_savings.credit(amount)
                    print(name + transaction_type + account_type + str(person_savings.AccountBalance))
                if element[1] == "Debit" and person_savings.AccountBalance >= amount:
                    person_savings.debit(amount) 
                    print(name + transaction_type + account_type + str(person_savings.AccountBalance))
            else: #if the acct type doesnt exist in our system present error
                print ("Account type not recognized, can not perform transaction!")
            #if the name dosn't exist then let user know
        except KeyError: 
            print ("Error! Account does not exist. ")
            

def banking(filename1, filename2):
    accounts = readFile(filename1)
    actions = readActionFile(filename2)
    dictionary1, dictionary2 = create_Checking_and_Savings(accounts)
    allTogether = transactions(actions, dictionary1, dictionary2)
    return allTogether