
class Transaction:
    def __init__(self, acc_num, s_code, price=40):
        self.service_charge = None
        self.acc_num = acc_num
        self.s_code = s_code
        self.price = price

    def set_acc_num(self, acc_num):
        self.acc_num = acc_num

    def get_acc_num(self):
        return self.acc_num

    def set_s_code(self, s_code):
        self.s_code = s_code

    def get_s_code(self):
        return self.s_code

    def payment(self, price, service_charge=10):
        self.service_charge = service_charge
        self.price = price + price*service_charge/100.00

    def get_price(self):
        return self.price
