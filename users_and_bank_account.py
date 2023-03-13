class BankAccount:
    all_accounts = []
    def __init__(self, user, acct_label, balance = 0):
        self.balance = balance
        self.acct_label = acct_label
        self.user = user
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds: charging $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    @classmethod
    def filter_accounts(cls, user):
        for obj in filter(lambda u: u.user == user, cls.all_accounts):
            print(vars(obj))
        return list(filter(lambda u: u.user == user, cls.all_accounts))
    
class User:
    all_users = []
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.accounts = []
        User.all_users.append(self)
    
    def open_new_account(self, acct_label, initial_deposit = 0):
        self.accounts.append(BankAccount(self.name, acct_label, initial_deposit))
        return self
    
    def make_deposit(self, label, amount):
        self.filter_user_accounts(label).balance += amount
        return self
    
    def make_withdrawal(self, label, amount):
        self.filter_user_accounts(label).balance -= amount
        return self
    

    def filter_user_accounts(self, acct_label):
        return list(filter(lambda u: u.acct_label == acct_label, self.accounts))[0]

    def display_user_balance(self):
        print(f"Balances for {self.name}")
        print('------------------------')
        for account in self.accounts:
            print(f"{account.acct_label} Balance: {account.balance}")
        print(' ')
        return self
    
    @classmethod
    def find_user(cls, user):
        filtered = filter(lambda obj: obj.name == user, cls.all_users)
        return list(filtered).pop()
    
    def transfer_money(self, amount, other_user, acct_label = 'Checking'):
        recipient = User.find_user(other_user)
        user_account = self.filter_user_accounts(acct_label)
        
        if amount > user_account.balance:
            print("Insufficient funds: Deducting $5 fee.")
            user_account.balance -= 5
        else:
            for acc in recipient.accounts:
                if acc.acct_label == acct_label:
                    acc.balance += amount
                    print(f"Update {acct_label} balance for {other_user}: {acc.balance}")
                    
            self.filter_user_accounts(acct_label).balance -= amount
            print(f"Update {acct_label} balance for {self.name}: {user_account.balance}")
            
    
    

user1 = User('Lucy Pevensie', 'lucy@narnia.com')
user2 = User('Edmond Pevensie', 'edmond@narnia.com')

user1.open_new_account('Checking', 500).open_new_account('Savings', 1000).make_deposit('Checking', 500).make_withdrawal('Savings', 50).display_user_balance()
user2.open_new_account('Checking').display_user_balance()

user1.transfer_money(100, 'Edmond Pevensie')
user2.transfer_money(5, 'Lucy Pevensie')