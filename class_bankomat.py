import time

class ATM:
    def __init__(self, pin, balance):
        self.pin = False
        self.balance = float(balance)
        self.history_trans = []

    def pinkod(self):
        pin = input("введите пароль:")
        if pin == "1234":
            self.pin = True
        else:
            print("неверный пароль")
            self.pin = False

    def menu(self):
        print("1 - проверить баланс", "2 - снять деньги", "3 - пополнить счет", "4 - история операций", "5 - выйти")

    def show_balance(self):
        if self.pin == True:
                print(self.balance)

    def minus(self):
        b = float(input("введите сумму:"))
        if b <= 0:
            print("сумма не может быть отрицательной")
        if b <= self.balance:
            print("операция прошла успешно!")
            self.balance -= b
            self.history_trans.append(f"Снятие {b}$")
            if b > self.balance:
                print("недостаточно средств")

    def plus(self):
        y = float(input("введите сумму:"))
        if y <= 0:
            print("сумма не может быть отрицательной")
        print("операция прошла успешно!")
        self.balance += y
        self.history_trans.append(f"пополнение {y}$")

    def history(self):
        for trans in self.history_trans:
            print(trans)
            print(time.ctime())

    def work(self):
        if self.pin == True:
            self.menu()
            command = input("введите:")
            if command == "1":
                self.show_balance()
            elif command == "2":
                self.minus()
            elif command == "3":
                self.plus()
            elif command == "4":
                self.history()
            elif command == "5":
                global status
                status = False

atm = ATM(True, "1000")
atm.pinkod()
status = True
while status:
    atm.work()
