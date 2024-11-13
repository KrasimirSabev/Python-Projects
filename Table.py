class Table:
    def __init__(self, total_tables=10):
        self.available_tables = total_tables

    def set_total_tables(self, total_tables):
        self.available_tables= total_tables

    def get_total_tables(self):
        return self.available_tables

    def available_table(self, customer_table, exception='Sorry, we do not have any more available tables'):
        if self.available_tables <= 0:
            print(exception)
            return False #returns false so it will not successfully make a reservation.
        elif customer_table > self.available_tables:
            print(f'Sorry, we only have {self.available_tables} tables available.')
            return False #similarly to before.
        if customer_table in [1,2]:
            self.available_tables -= customer_table
            print(f'There are {self.available_tables} tables remaining.')
            return True #here True refers to successfully making a reservation.
        else:
            print('Invalid table size.')
            return False