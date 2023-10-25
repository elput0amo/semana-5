class BankAccount:
    def __init__(self, account_number,pasta ):
       self. account_number = account_number
       self. pasta= pasta
    def conseguir_el_numerito (self):
        return self. account_number
    def cuanto_tienes(self):
        return self.pasta
    def deposit(self, fondos):
        self.pasta += fondos
    def extraer( self, efectivo):
        self.pasta -= efectivo
