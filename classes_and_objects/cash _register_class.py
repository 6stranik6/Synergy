class CashRegister:
    def __init__(self, start_amount):
        self.amount = start_amount

    def top_up(self, amount):
        self.amount += amount

    def count_1000(self):
        if self.amount % 1000 == 0:
            print(f"В кассе осталось {self.amount // 1000} тысяч")
        else:
            print(f"В кассе осталось {self.amount // 1000} тысяч и {self.amount % 1000} рублей")

    def take_away(self, amount):
        if self.amount >= amount:
            self.amount -= amount
        else:
            print("Недостаточно денег в кассе")

cash_drawer = CashRegister(5000)
cash_drawer.top_up(2000)
cash_drawer.count_1000()
cash_drawer.take_away(8000)
cash_drawer.count_1000()