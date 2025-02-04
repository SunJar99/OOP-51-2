class BankAccount:
    def __init__(self, client, balance, password):
        self.client = client # Open
        self._balance = balance # Safe
        self.__password = password # Private
    
    def __top_up_balance(self._balance, amount):
        
    def about(self):
        print(f"PS: {self.__password}")

client = BankAccount("John Doe", 1000, 123456)
