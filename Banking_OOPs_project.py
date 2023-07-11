class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print('')
        print('Personal Details: ')
        print('')
        print("Name:", self.name)
        print("gender:", self.gender)
        print("Age:", self.age)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("The Current account balance is: $",self.balance)
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print('Sorry, Isufficient Balance, current balance: $', self.balance)
        else:
            self.balance = self.balance - self.amount
            print("The Current account balance is: $", self.balance)
    def curr_bal(self):
        self.details()
        print("The Current account balance is: $", self.balance)

a = Bank('Chief', 16, "Male")
a.deposit(2000)
a.withdraw(2500)
a.details()
a.curr_bal()
