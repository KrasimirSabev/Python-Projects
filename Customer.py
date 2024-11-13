class Customer:
    def __init__(self, customer_id, fname, lname, age=0):
        self.customer_id = customer_id
        self.fname = fname
        self.lname = lname
        self.age = age

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_fname(self, fname):
        self.fname = fname

    def get_fname(self):
        return self.fname

    def set_lname(self, lname):
        self.lname = lname

    def get_lname(self):
        return self.lname

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_customer_id(self):
        return self.customer_id
