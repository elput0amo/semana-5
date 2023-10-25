class BankAccount:
    def __init__(self, account_number,pasta = 0):
       self. account_number = account_number
       self. pasta= pasta
    def conseguir_el_numerito (self):
        return self. account_number
    def cuanto_tienes(self):
        return self.pasta
    def deposit(self, fondos):
        self.pasta += fondos

class SavingsAccount (BankAccount):
    def __init__(self, account_number,pasta = 0, interes= 2):
       super().__init__(account_number, pasta )
       self. interes = 5
    def intereses (self,month):
        self.month=month
        month= input(f"Cuantos meses lleva el dinero: ")
        ahorro= self.pasta*self.interes/100
        return ahorro
