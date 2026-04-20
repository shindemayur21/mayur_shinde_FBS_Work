class BankAccount:
    branch = 'Kotak'

    def __init__(self, ac_no, bal, holder_name):
        self.ac_no = ac_no
        self.bal = bal
        self.holder_name = holder_name

    def display(self):
        return f'Account No: {self.ac_no}\nBalance: {self.bal}\nHolder Name : {self.holder_name}\nBranch Name : {self.branch}'


    @staticmethod
    def displayBranch():
        return BankAccount.branch


b1 = BankAccount(100, 15000, 'Mayur Shinde')
b2 = BankAccount(101, 20000, 'Shinde Mayur')

res = b1.display()
print(res)
print(f'######################################################')
res = b2.display()
print(res)
print(f'######################################################')
print(BankAccount.displayBranch())
print(b1.displayBranch())