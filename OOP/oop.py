import datetime
import pytz
# try use double underscore mangling balance

class account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        self.transaction_list.append((account.current_time(),balance))
        print("Account has been made for {}".format(name))
    @staticmethod
    def current_time():
        utc_time = datetime.datetime.utcnow()
        print(pytz.utc.localize(utc_time))
        return pytz.utc.localize(utc_time)

    def deposit(self,amount):
        self.balance += amount
        self.show_bal()
        self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.show_bal()
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), -amount))
        else:
            print("Can't withdraw amount no sufficient funds")
            self.show_bal()

    def show_bal(self):
        print("Balance is {}".format(self.balance))


    def show_trans(self):
        for date , amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {}".format(amount,tran_type,date,date.astimezone))
    # def initial_bal(self):
    #     current = self.balance
    #     print("Initial balance is {}".format(current))
    #

amr = account( "Amr" , 500 )
amr.show_bal()
amr.deposit(1000)
amr.withdraw(1600)
amr.withdraw(600)
amr.show_trans()

steph = account( "Steph" , 800 )
steph._balance = 40
steph.deposit( 100 )
steph.withdraw( 200 )
steph.show_trans( )
steph.show_bal()
# steph._account._balance = 40
# steph.show_bal()
# print(steph.__dict__)