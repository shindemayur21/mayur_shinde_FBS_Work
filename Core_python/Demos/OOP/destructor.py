class BankAccount:
    def __init__(self, ac_no, bal, holder_name):
        self.ac_no = ac_no
        self.bal = bal
        self.holder_name = holder_name

    def display(self):
        return f'Account No: {self.ac_no}\nBalance: {self.bal}\nHolder Name : {self.holder_name}'
    
    def __del__(self):
        return 'This is destructor....'

b1 = BankAccount(100, 15000, 'Mayur Shinde')
# b1.display()
# del b1
res = b1.display()
print(res)