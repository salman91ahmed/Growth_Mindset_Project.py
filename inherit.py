from dataclasses import dataclass

# @dataclass()

# class enginerr():
#     name : str 
#     age : str
    



# @dataclass()

# class person(enginerr):

#     skill:str



# @dataclass()
# class Bank():
#     id: str
#     username: str
#     accountnumber: str
#     amount:int


# @dataclass()
# class User(Bank):
#    username: str

# result = User(id="12",username="ali",accountnumber=123123,amount="120000",age="12")
# print(result) 








@dataclass
class Account():
    name : str
    account_number: int
    balance:int= 500
    def deposit(self,amount:int):
        self.balance = amount+self.balance
        print("deposit amount",self.balance)

    def withdraw(self,amount:int):
        self.balance = self.balance - amount
        if amount > self.balance:
            print(f"depositing {self.balance}")

        else:
            self.balance = self.balance - amount
            print(f"withdraw {amount}")


 
ameen:Account = Account('waleed',12) 
ameen.deposit(100)





@dataclass
class Current_Account(Account):
    overdraft_Limit: int = 1000
    def withdraw(self,amount:int):
        self.balance = self.balance +self.overdraft_Limit
        if amount > self.balance:
            print(f"depositing {self.balance}")

        else:
            self.balance = self.balance - amount
            print(f"withdraw {amount}")
    

ameen = Current_Account("Ameen",1234567890)
ameen.withdraw(1500)
print(ameen.balance, "ameen balance") 
